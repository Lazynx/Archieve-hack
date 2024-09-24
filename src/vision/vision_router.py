# vision_router.py

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from vision_service import VisionService

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
        results = await vision_service.analyze_image(contents)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при анализе изображения: {str(e)}")
