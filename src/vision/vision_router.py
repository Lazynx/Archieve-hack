# vision_router.py

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from .vision_service import VisionService
from src.openai.openai_service import process_text_with_gpt

router = APIRouter()

def get_vision_service():
    try:
        return VisionService()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при инициализации VisionService: {str(e)}")


@router.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...),
    vision_service: VisionService = Depends(get_vision_service)
):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Загруженный файл не является изображением.")

    contents = await file.read()
    try:
        # Извлекаем текст из изображения
        ocr_results = await vision_service.analyze_image(contents)
        extracted_text = ocr_results.get('text', '')

        if not extracted_text:
            raise HTTPException(status_code=400, detail="Не удалось извлечь текст из изображения.")

        # Обрабатываем текст через OpenAI API
        transformed_text = await process_text_with_gpt(extracted_text)

        return {"transformed_text": transformed_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при анализе изображения: {str(e)}")
