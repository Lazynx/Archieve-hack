# vision_service.py

from google.cloud import vision
from google.oauth2 import service_account
import os

class VisionService:
    def __init__(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            credentials_path = os.path.join(current_dir, 'credentials.json')
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            self.client = vision.ImageAnnotatorClient(credentials=credentials)
        except Exception as e:
            print(f"Ошибка при инициализации VisionService: {e}")
            raise

    async def analyze_image(self, image_content: bytes):
        image = vision.Image(content=image_content)

        response = self.client.annotate_image({
            'image': image,
            'features': [
                {'type_': vision.Feature.Type.LABEL_DETECTION},
                {'type_': vision.Feature.Type.OBJECT_LOCALIZATION},
                {'type_': vision.Feature.Type.FACE_DETECTION},
                {'type_': vision.Feature.Type.IMAGE_PROPERTIES},
                {'type_': vision.Feature.Type.TEXT_DETECTION},
            ],
        })

        results = {
            'labels': [label.description for label in response.label_annotations],
            'objects': [obj.name for obj in response.localized_object_annotations],
            'faces': len(response.face_annotations),
            'dominant_colors': [
                {
                    'color': f'#{int(color.color.red):02x}{int(color.color.green):02x}{int(color.color.blue):02x}',
                    'score': color.score,
                    'pixel_fraction': color.pixel_fraction,
                }
                for color in response.image_properties_annotation.dominant_colors.colors[:5]
            ],
            'text': response.full_text_annotation.text if response.full_text_annotation.text else ''
        }

        return results
