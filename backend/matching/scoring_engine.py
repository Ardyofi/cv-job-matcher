from sklearn.metrics.pairwise import cosine_similarity
from ..nlp.skill_extractor import extract_skills
from ..nlp.vectorizer import vectorize_texts

def compute_match_score(cv_text: str, job_text: str) -> float:
    # Skill overlap
    cv_skills = set(extract_skills(cv_text))
    job_skills = set(extract_skills(job_text))
    skill_score = len(cv_skills & job_skills) / (len(job_skills) or 1)

    # Semantic similarity (TF-IDF cosine)
    vectors = vectorize_texts([cv_text, job_text])
    semantic_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Combine
    final_score = 0.5 * skill_score + 0.5 * semantic_score
    return round(final_score, 2)