from fastapi import APIRouter
from src.aws.router import router as aws_router
from src.latex.router import router as latex_router

router = APIRouter()

# router.include_router(perfume_router, prefix="/perfume")
router.include_router(aws_router, prefix="/aws")

router.include_router(latex_router, prefix="/latex")