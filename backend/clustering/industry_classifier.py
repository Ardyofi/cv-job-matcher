from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from backend.text_extraction.pdf_parser import extract_text_from_pdf
from backend.text_extraction.docx_parser import extract_text_from_docx

INDUSTRY_KEYWORDS = ["software", "data", "finance", "marketing", "healthcare", "education"]

def classify_industry(job_files):
    texts = []
    filenames = []

    for job in job_files:
        text = extract_text_from_pdf(job) if job.filename.endswith(".pdf") else extract_text_from_docx(job)
        texts.append(text)
        filenames.append(job.filename)

    # TF-IDF + KMeans
    vectorizer = TfidfVectorizer(vocabulary=INDUSTRY_KEYWORDS)
    X = vectorizer.fit_transform(texts)
    kmeans = KMeans(n_clusters=len(INDUSTRY_KEYWORDS), random_state=42)
    labels = kmeans.fit_predict(X)

    result = {}
    for i, label in enumerate(labels):
        industry = INDUSTRY_KEYWORDS[label]
        if industry not in result:
            result[industry] = []
        result[industry].append(filenames[i])
    return result