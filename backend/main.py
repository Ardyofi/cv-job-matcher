from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="CV Job Matcher")

app.include_router(router)