import subprocess
import os
import tempfile

# def convert_tex_to_pdf(tex_file_path):
#     # Ensure the file exists
#     if not os.path.exists(tex_file_path):
#         print("The specified .tex file does not exist.")
#         return None
    
#     # Run pdflatex command
#     try:
#         subprocess.run(['pdflatex', tex_file_path], check=True)
#         print(f"PDF generated from {tex_file_path}")
        
#         # The output PDF file will have the same name as the .tex file
#         pdf_file_path = tex_file_path.replace('.tex', '.pdf')
#         return pdf_file_path
#     except subprocess.CalledProcessError as e:
#         print("Error occurred during the PDF generation.")
#         return None

# # Usage example
# tex_file = '/home/seveneleven/pythonProjects/Archieve-hack/src/latex/fotka.tex'
# pdf_file = convert_tex_to_pdf(tex_file)
# if pdf_file:
#     print(f"PDF successfully created at: {pdf_file}")


def convert_tex_to_pdf_from_response(response):
    # Получаем LaTeX-код из JSON response
    latex_code = response.get("response")

    if not latex_code:
        print("No LaTeX content found in the response.")
        return None
    
    # Используем временные файлы для работы с LaTeX
    try:
        with tempfile.NamedTemporaryFile(suffix=".tex", delete=False) as temp_tex_file:
            # Записываем LaTeX-код во временный .tex файл
            temp_tex_file.write(latex_code.encode('utf-8'))
            temp_tex_file_path = temp_tex_file.name
        
        # Создаем временный файл для PDF
        temp_pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        temp_pdf_file_path = temp_pdf_file.name
        temp_pdf_file.close()  # Закрываем файл, чтобы pdflatex мог его использовать

        # Запускаем pdflatex для генерации PDF
        try:
            subprocess.run(
                ['pdflatex', '-output-directory', os.path.dirname(temp_tex_file_path), temp_tex_file_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"PDF generated successfully from LaTeX content.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during PDF generation: {e}")
            return None
        
        # Читаем сгенерированный PDF и возвращаем его содержимое
        with open(temp_pdf_file_path.replace('.tex', '.pdf'), 'rb') as pdf_file:
            pdf_content = pdf_file.read()

        # Удаляем временные файлы после использования
        os.remove(temp_tex_file_path)
        os.remove(temp_pdf_file_path)

        return pdf_content
    
    except Exception as e:
        print(f"Error: {e}")
        return None