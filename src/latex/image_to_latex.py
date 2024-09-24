from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = """
Тебе дан фото с документом. Напиши код LaTeX, где только структура документа. Твой ответ должен содержать только LaTeX код. Не используй ``` для блока кода. Убедись, что код компилируется без ошибок в LaTeX.
Не забудь такие параметры как:
\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{graphicx}
\\usepackage[T2A]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[russian]{babel}
"""

async def get_latex_code_from_image(image_url: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": system_prompt},
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
        print(system_prompt)
        json_response = {
            "response": response.choices[0].message.content,
            "status": 200,
        }
        print(json_response.get("response"))
        return json_response
    except Exception as e:
        return {
            "response": str(e),
            "status": 500,
        }