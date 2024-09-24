import subprocess
import os

def convert_tex_to_pdf(tex_file_path):
    # Ensure the file exists
    if not os.path.exists(tex_file_path):
        print("The specified .tex file does not exist.")
        return None
    
    # Run pdflatex command
    try:
        subprocess.run(['pdflatex', tex_file_path], check=True)
        print(f"PDF generated from {tex_file_path}")
        
        # The output PDF file will have the same name as the .tex file
        pdf_file_path = tex_file_path.replace('.tex', '.pdf')
        return pdf_file_path
    except subprocess.CalledProcessError as e:
        print("Error occurred during the PDF generation.")
        return None

# Usage example
tex_file = '/home/seveneleven/pythonProjects/Archieve-hack/src/latex/fotka.tex'
pdf_file = convert_tex_to_pdf(tex_file)
if pdf_file:
    print(f"PDF successfully created at: {pdf_file}")
