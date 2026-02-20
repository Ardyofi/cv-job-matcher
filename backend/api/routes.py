from fastapi import APIRouter, UploadFile, File
from text_extraction.pdf_parser import extract_text_from_pdf
from text_extraction.docx_parser import extract_text_from_docx

router = APIRouter()

@router.post("/upload-cv/")
async def upload_cv(file: UploadFile = File(...)):
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(file.file)
    else:
        return {"error": "Unsupported file format"}

    return {"filename": file.filename, "text_length": len(text)}