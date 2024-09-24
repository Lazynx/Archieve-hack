from fastapi import APIRouter
from src.aws.router import router as aws_router

router = APIRouter()

# router.include_router(perfume_router, prefix="/perfume")
router.include_router(aws_router, prefix="/aws")
