import cv2
import numpy as np
import io
from PIL import Image
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Предполагается, что эти переменные уже определены где-то в вашем коде
s3_client = boto3.client('s3')

def enhance_image(image_bytes):
    try:
        # Преобразование байтов в изображение numpy
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            raise ValueError("Failed to decode image")

        # Применение различных методов улучшения
        # 1. Увеличение резкости
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        img = cv2.filter2D(img, -1, kernel)

        # 2. Улучшение контраста
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl,a,b))
        img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        # 3. Шумоподавление
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        # Преобразование обратно в байты
        is_success, buffer = cv2.imencode(".jpg", img)
        if not is_success:
            raise ValueError("Failed to encode image")
        
        return io.BytesIO(buffer).getvalue()
    except Exception as e:
        logger.error(f"Error in enhance_image: {str(e)}")
        raise

async def upload_file(bucket_name: str, file: bytes, file_name: str):
    try:
        # Проверка размера файла
        if len(file) > 5 * 1024 * 1024:  # например, 5MB
            logger.warning("File is too large")
            return None

        # Улучшение качества изображения
        enhanced_file = enhance_image(file)

        # Загрузка улучшенного изображения
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=enhanced_file
        )
        logger.info(f"File uploaded successfully: {file_name}")
        return f"https://{bucket_name}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
    except NoCredentialsError:
        logger.error("Credentials not available")
        return None
    except ClientError as e:
        logger.error(f"S3 ClientError: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error in upload_file: {str(e)}")
        return None

async def delete_file(bucket_name: str, file_name: str):
    try:
        response = s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        logger.info(f"File deleted successfully: {file_name}")
        return True
    except ClientError as e:
        logger.error(f"Error deleting file {file_name}: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error in delete_file: {str(e)}")
        return False
    
