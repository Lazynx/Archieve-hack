from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image
import io
import requests
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

    def image_to_bytes(self, image_url):
        try:
            # Загружаем изображение по URL
            response = requests.get(image_url, timeout = 10)
            response.raise_for_status() 
            img = Image.open(io.BytesIO(response.content))

             # Получаем исходный формат изображения
            img_format = img.format

        # Конвертируем изображение в байты, используя исходный формат
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format=img_format)  # Используем исходный формат изображения
            img_bytes = img_byte_array.getvalue()

            

            return img_bytes
        except Exception as e:
            print(f"Ошибка при загрузке или преобразовании изображения: {e}")
            raise

    async def analyze_image(self, image_url):
        # Преобразуем изображение в байты
        image_content = self.image_to_bytes(image_url)

        # Создаем объект изображения для Google Vision API
        image = vision.Image(content=image_content)

        # Отправляем изображение на анализ
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




