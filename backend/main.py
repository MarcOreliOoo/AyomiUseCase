#python -m uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from RPN import evaluate_rpn

app = FastAPI()

class Expression(BaseModel):
	expression: str

@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello": "World"}

@app.get("/rpn/{expression}")
async def calcRPN(expression: str):
    try: 
        return {"result": evaluate_rpn(expression)}
    except (ValueError, TypeError) as e: 
        return {"error": str(e)}

@app.post("/rpn")
async def calcRPN(expression: Expression):
    return {"result": evaluate_rpn(expression.expression)}

@app.get("/download", response_class=FileResponse)
async def download():
	filePath = "path/to/data.csv"
	response = FileResponse(filePath, media_type="text/csv")
	response.headers["Content-Disposition"] = "attachment; filename=data.csv"
	return response