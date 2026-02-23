from backend.matching.scoring_engine import compute_match_score
from backend.text_extraction.pdf_parser import extract_text_from_pdf
from backend.text_extraction.docx_parser import extract_text_from_docx

def compare_cvs(cv1_file, cv2_file, job_files):
    results = []
    for job in job_files:
        job_text = extract_text_from_pdf(job) if job.filename.endswith(".pdf") else extract_text_from_docx(job)
        cv1_text = extract_text_from_pdf(cv1_file) if cv1_file.filename.endswith(".pdf") else extract_text_from_docx(cv1_file)
        cv2_text = extract_text_from_pdf(cv2_file) if cv2_file.filename.endswith(".pdf") else extract_text_from_docx(cv2_file)

        cv1_score = compute_match_score(cv1_text, job_text)
        cv2_score = compute_match_score(cv2_text, job_text)
        winner = "cv1" if cv1_score > cv2_score else "cv2" if cv2_score > cv1_score else "tie"

        results.append({
            "job": job.filename,
            "cv1_score": cv1_score,
            "cv2_score": cv2_score,
            "winner": winner
        })
    return results