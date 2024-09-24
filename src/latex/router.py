from fastapi import APIRouter
from src.latex.model import LatexModel
from src.latex.openai_service import get_latex_code_from_image

router = APIRouter()

@router.post("/latex_code")
async def get_latex_code(image_model: LatexModel):
    return await get_latex_code_from_image(image_url=image_model.image_url)

