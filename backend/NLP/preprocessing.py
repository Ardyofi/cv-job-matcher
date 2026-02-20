import re

def preprocess_text(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove special chars
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text