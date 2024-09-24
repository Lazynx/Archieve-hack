from fastapi import APIRouter, HTTPException, Response
from src.latex.model import LatexModel
from src.latex.image_to_latex import get_latex_code_from_image
from src.latex.latex_to_pdf import convert_tex_to_pdf_from_response

router = APIRouter()

@router.post("/latex_code")
async def get_latex_code(image_model: LatexModel):
    try:
        json_response = await get_latex_code_from_image(image_url=image_model.image_url)
        
        if json_response["status"] != 200:
            raise HTTPException(status_code=500, detail="Failed to generate LaTeX code from image.")
        
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
