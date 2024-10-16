# vision_router.py

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Query, Response
from src.vision.vision_service import VisionService
from src.openai.openai_service import get_image_description
from src.latex.image_and_text_to_latex import get_latex_code_from_image_and_text
from src.latex.image_to_latex import get_latex_code_from_image
from src.latex.latex_to_pdf import convert_tex_to_pdf_from_response
from src.aws.s3_service import upload_file
from typing import Annotated
import uuid

router = APIRouter()

def get_vision_service():
    try:
        return VisionService()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при инициализации VisionService: {str(e)}")


@router.post("/analyze")
async def analyze_imageio(
    file: UploadFile = File(...),
    vision_service: VisionService = Depends(get_vision_service)
):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Загруженный файл не является изображением.")

    contents = await file.read()
    try:
        ocr_results = await vision_service.analyze_image(contents)
        extracted_text = ocr_results.get('text', '')

        if not extracted_text:
            raise HTTPException(status_code=400, detail="Не удалось извлечь текст из изображения.")

        transformed_text = await get_image_description(extracted_text)

        return {"transformed_text": transformed_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при анализе изображения: {str(e)}")

@router.get("/analyze-url")
async def analyze_image_by_url(
    image_url: str = Query(..., description="URL изображения для анализа"),
    vision_service: VisionService = Depends(get_vision_service)
):
    try:
        ocr_results = await vision_service.analyze_image(image_url)
        extracted_text = ocr_results.get('text', '')

        if not extracted_text:
            raise HTTPException(status_code=400, detail="Не удалось извлечь текст из изображения.")

        json_response = await get_latex_code_from_image_and_text(image_url=image_url, provided_text=extracted_text)
        
        if json_response["status"] != 200:
            raise HTTPException(status_code=500, detail="Failed to generate LaTeX code from image and text.")

        try:
            pdf_content = convert_tex_to_pdf_from_response(json_response)
        except Exception as pdf_error:
            raise HTTPException(status_code=500, detail=f"PDF generation failed with error: {str(pdf_error)}")

        if not pdf_content:
            raise HTTPException(status_code=500, detail="Failed to generate PDF from LaTeX code: Empty content.")
        
        return Response(content=pdf_content, media_type="application/pdf")

    except HTTPException as http_err:
        raise http_err  
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@router.post("/get_pdf")
async def analyze_image(
        file: Annotated[UploadFile, File(...)],
        vision_service: VisionService = Depends(get_vision_service)
):
    try:
        file_name = f"{uuid.uuid4()}{file.filename}"

        file_content = await file.read()

        bucket_name = "spotify-nf"
        print("GRUZIM V AWS")
        s3_url = await upload_file(bucket_name, file_content, file_name)

        if not s3_url:
            raise HTTPException(status_code=500, detail="Failed to upload file to S3")

        print("POLUchaem pdf")
        result = await analyze_image_by_url(s3_url, vision_service)

        return result

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")