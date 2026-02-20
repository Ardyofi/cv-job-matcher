from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="CV Job Matcher API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "CV Job Matcher API is running"}