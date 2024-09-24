# src/openai_service.py
from openai import OpenAI
from config import OPENAI_API_KEY
import re

client = OpenAI(api_key=OPENAI_API_KEY)

async def get_image_description(image_url: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                    },
                ],
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)


async def process_text_with_gpt(text: str) -> str:
    try:
        system_prompt = "Вы — помощник, который помогает исправлять текст. Ваша задача — исправить ошибки и опечатки в тексте, а также расшифровать скомканные или нечеткие части. Преобразуйте неполные или спутанные фрагменты в связные предложения." \
                        "Руководство: " \
                        " 1. Исправление ошибок: Исправляйте все грамматические, орфографические и пунктуационные ошибки." \
                        "2. Расшифровка: Преобразуйте непонятные или неразборчивые части текста в осмысленные фразы. Например, текст “э 0\nорганизации и их ком-частьХлопстроя заверило” преобразуется в “Организации и их ком-часть Хлопстроя заверило”." \
                        "3. Имена и названия: Не изменяйте имена, фамилии и названия организаций." \
                        "4. Устранение символов: Удаляйте все специальные символы, такие как ‘\n’ и ‘\n\n’, чтобы текст был плавным и естественным." \
                        "5. Целостность текста: Убедитесь, что текст читается естественно, с правильной грамматикой и пунктуацией. Убирайте переносы строк, создавая непрерывный текст."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text},
                    ],
                }
            ],
        )
        transformed_text = response.choices[0].message.content

        transformed_text = re.sub(r'\n+', ' ', transformed_text).strip()

        return transformed_text
    except Exception as e:
        return str(e)