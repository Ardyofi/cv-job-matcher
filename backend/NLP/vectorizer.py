from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def vectorize_texts(texts):
    return vectorizer.fit_transform(texts)