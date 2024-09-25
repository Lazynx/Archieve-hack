from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = """
Тебе дано фото с документом, а также текст, который изображен на фото. Напиши код LaTeX, используя данный текст, где только структура документа по фото. Ты обязан соблюдать структуру документа и текста. Твой ответ должен содержать только LaTeX код. Не используй ``` для блока кода. Убедись, что код компилируется без ошибок в LaTeX.
Не забудь такие параметры как:
\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{graphicx}
\\usepackage[T2A]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[russian]{babel}
"""

async def get_latex_code_from_image_and_text(image_url: str, provided_text: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"Вот ссылка на изображение: {image_url}. А вот текст, который изображен на фото:\n\n{provided_text}"
                }
            ],
        )
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
