from .preprocessing import preprocess_text

SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "machine learning",
    "data analysis", "fastapi", "docker", "aws"
]

def extract_skills(text: str):
    text = preprocess_text(text)
    skills = [skill for skill in SKILL_KEYWORDS if skill in text]
    return skills