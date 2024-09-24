# global_router.py

from fastapi import APIRouter
from src.vision.vision_router import router as vision_router
from src.aws.router import router as aws_router
from src.latex.router import router as latex_router

router = APIRouter()

# Подключаем роутер vision
router.include_router(vision_router, prefix="/vision", tags=["vision"])

# Подключаем другие роутеры при необходимости
router.include_router(aws_router, prefix="/aws")

router.include_router(latex_router, prefix="/latex")
