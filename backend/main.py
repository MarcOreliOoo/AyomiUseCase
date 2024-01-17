#python -m uvicorn backend.main:app --reload
from fastapi import FastAPI
from backend.db.database import create_db_and_tables

from backend.routers import rpn

app = FastAPI()
app.include_router(rpn.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/health", include_in_schema=False)
def read_root():
    return {"Hello": "WORLD"}