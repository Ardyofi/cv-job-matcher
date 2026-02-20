from fastapi import APIRouter, UploadFile, File
from typing import List
from backend.text_extraction.pdf_parser import extract_text_from_pdf
from backend.text_extraction.docx_parser import extract_text_from_docx
from backend.matching.scoring_engine import compute_match_score
from backend.matching.comparison_engine import compare_cvs
from backend.clustering.industry_classifier import classify_industry

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "CV Job Matcher API is running"}

@router.post("/upload/cvs")
async def upload_cvs(files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]
    return {"uploaded_files": filenames}

@router.post("/upload/jobs")
async def upload_jobs(files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]
    return {"uploaded_jobs": filenames}

@router.post("/match")
async def match_cv_job(cv: UploadFile = File(...), job: UploadFile = File(...)):
    cv_text = extract_text_from_pdf(cv)
    job_text = "dummy job text"
    score = compute_match_score(cv_text, job_text)
    return {"score": score}

@router.post("/compare")
async def compare_cv_files(cv1: UploadFile = File(...), cv2: UploadFile = File(...), jobs: List[UploadFile] = File(...)):
    result = compare_cvs(cv1, cv2, jobs)
    return result

@router.post("/industry-fit")
async def industry_fit(jobs: List[UploadFile] = File(...)):
    result = classify_industry(jobs)
    return result