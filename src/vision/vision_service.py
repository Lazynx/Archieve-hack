from google.cloud import vision
from google.oauth2 import service_account
import src.openai.openai_service
import os
from config import (
    GOOGLE_TYPE,
    GOOGLE_PROJECT_ID,
    GOOGLE_PRIVATE_KEY_ID,
    GOOGLE_PRIVATE_KEY,
    GOOGLE_CLIENT_EMAIL,
    GOOGLE_CLIENT_ID,
    GOOGLE_AUTH_URI,
    GOOGLE_TOKEN_URI,
    GOOGLE_AUTH_PROVIDER_X509_CERT_URL,
    GOOGLE_CLIENT_X509_CERT_URL,
)


class VisionService:
    def __init__(self):
        try:
            credentials_info = {
                "type": GOOGLE_TYPE,
                "project_id": GOOGLE_PROJECT_ID,
                "private_key_id": GOOGLE_PRIVATE_KEY_ID,
                "private_key": GOOGLE_PRIVATE_KEY,
                "client_email": GOOGLE_CLIENT_EMAIL,
                "client_id": GOOGLE_CLIENT_ID,
                "auth_uri": GOOGLE_AUTH_URI,
                "token_uri": GOOGLE_TOKEN_URI,
                "auth_provider_x509_cert_url": GOOGLE_AUTH_PROVIDER_X509_CERT_URL,
                "client_x509_cert_url": GOOGLE_CLIENT_X509_CERT_URL,
            }
            # Создание объекта Credentials из словаря
            credentials = service_account.Credentials.from_service_account_info(credentials_info)
            self.client = vision.ImageAnnotatorClient(credentials=credentials)
        except Exception as e:
            print(f"Ошибка при инициализации VisionService: {e}")
            raise

    async def analyze_image(self, image_content: bytes):
        image = vision.Image(content=image_content)

        response = self.client.annotate_image({
            'image': image,
            'features': [
                {'type_': vision.Feature.Type.TEXT_DETECTION},
            ],
        })

        print(response.full_text_annotation.text)
        results = {
            'text': response.full_text_annotation.text if response.full_text_annotation.text else ''
        }

        return results
