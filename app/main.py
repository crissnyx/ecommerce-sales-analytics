from fastapi import FastAPI
from backend.app.api.v1.api import api_router
from backend.app.db.session import create_db_and_tables

app = FastAPI(title="Ecommerce SaaS API", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

@app.get("/health")
def health_check():
    return {"status": "ok"}
