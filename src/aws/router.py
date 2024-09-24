# src/aws/router.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from src.aws.s3_service import upload_file, delete_file
from src.openai.openai_service import get_image_description
import uuid

router = APIRouter()

BUCKET_NAME = "spotify-nf"


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Generate a unique file name
        file_name = f"images/{uuid.uuid4()}-{file.filename}"

        # Upload file to S3
        file_url = await upload_file(BUCKET_NAME, await file.read(), file_name)

        if not file_url:
            raise HTTPException(status_code=500, detail="File upload failed")

        # Send the file URL to OpenAI GPT for description
        description = await get_image_description(file_url)

        return {
            "file_url": file_url,
            "description": description
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))