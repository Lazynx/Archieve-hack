from fastapi import APIRouter
from src.latex.model import LatexModel
from src.latex.openai_service import get_latex_code_from_image

router = APIRouter()

@router.post("/latex_code")
async def get_latex_code(image_model: LatexModel):
    json_response = await get_latex_code_from_image(image_url=image_model.image_url)

    if json_response["status"] != 200:
        raise HTTPException(status_code=500, detail="Failed to generate LaTeX code from image.")
    
    pdf_content = convert_tex_to_pdf_from_response(json_response)

    if not pdf_content:
        raise HTTPException(status_code=500, detail="Failed to generate PDF from LaTeX code.")
    
    return {
        "message": "PDF generated successfully",
        "pdf_content": pdf_content  # Здесь возвращается PDF контент (в реальном мире можно использовать fastapi.responses.FileResponse)
    }