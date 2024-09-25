import subprocess
import os
import tempfile

def convert_tex_to_pdf_from_response(response):
    latex_code = response.get("response")

    if not latex_code:
        print("No LaTeX content found in the response.")
        return None
    
    try:
        with tempfile.NamedTemporaryFile(suffix=".tex", delete=False) as temp_tex_file:
            temp_tex_file.write(latex_code.encode('utf-8'))
            temp_tex_file_path = temp_tex_file.name

        print(f"Temporary LaTeX file created at: {temp_tex_file_path}")
        
        try:
            result = subprocess.run(
                ['pdflatex', '-output-directory', os.path.dirname(temp_tex_file_path), temp_tex_file_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            print(result.stderr.decode('utf-8'))
            print(f"PDF generated successfully from LaTeX content.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during PDF generation: {e}")
            print(f"Standard output: {e.stdout.decode('utf-8')}")
            print(f"Standard error: {e.stderr.decode('utf-8')}")
            return None
        
        pdf_file_path = os.path.join(os.path.dirname(temp_tex_file_path), os.path.basename(temp_tex_file_path).replace('.tex', '.pdf'))
        print(f"Looking for PDF at: {pdf_file_path}")

        if not os.path.exists(pdf_file_path):
            print("PDF file was not created.")
            return None

        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()

        os.remove(temp_tex_file_path)
        os.remove(pdf_file_path)

        return pdf_content
    
    except Exception as e:
        print(f"Error: {e}")
        return None
