from docx import Document

def contenido_word(archivo):
    try:
        doc = Document(archivo)

        print("Contenido del archivo:")
        for para in doc.paragraphs:
            print(para.text)

    except Exception as e:
        print(f"Error al abrir el archivo Word: {e}")

archivo_word = 'word.docx'
contenido_word(archivo_word)
