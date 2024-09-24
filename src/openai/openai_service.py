# src/openai_service.py
from openai import OpenAI
from config import OPENAI_API_KEY

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
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)
