from docx import Document

def extract_text_from_docx(file):
    doc = Document(file.file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text