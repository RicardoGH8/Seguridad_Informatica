import PyPDF2

def contenido_pdf(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            print(f"Contenido del archivo '{nombre_archivo}':")
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                print(f"--- Página {page_num + 1} ---")
                print(text)

    except Exception as e:
        print(f"Error al abrir el archivo PDF: {e}")

archivo_pdf = 'word.pdf'
contenido_pdf(archivo_pdf)
