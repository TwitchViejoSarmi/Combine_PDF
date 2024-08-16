from PyPDF2 import PdfWriter
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    pdf_path = os.getenv("PDF_PATH")
    new_pdf = PdfWriter() # Crear un objeto para escritura de pdf.
    for root, _, files in os.walk(pdf_path):
        for file in files:
            new_pdf.append(f"{root}/{file}") # Agregar los pdfs encontrados al nuevo pdf.

    try:
        os.makedirs('output/')
    except FileExistsError:
        pass
    new_pdf.write("output/output.pdf") # Unir los pdfs recolectados.
    new_pdf.close()

    os.system("cls")
    print("SE HAN JUNTADO LOS ARCHIVOS CORRECTAMENTE!")
    os.system("pause")
main()