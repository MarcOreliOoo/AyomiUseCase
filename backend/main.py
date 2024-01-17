#python -m uvicorn main:app --reload
from fastapi import FastAPI


from backend.routers import rpn

app = FastAPI()
app.include_router(rpn.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello": "World"}