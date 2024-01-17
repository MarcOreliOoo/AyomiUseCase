#python -m uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from RPN import evaluate_rpn

import pandas as pd
import io

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

@app.get("/download", response_class=StreamingResponse)
async def download():
	data = pd.DataFrame([{"expression":"1 2 +","result":"3"},{"expression":"2 3 *","result":"6"},{"expression":"2 3 + 4 *","result":"20"}])
	stream = io.StringIO()
	data.to_csv(stream, index=False)
	response = StreamingResponse(
		iter([stream.getvalue()]), media_type="text/csv")
	response.headers["Content-Disposition"] = "attachment; filename=data.csv"
	return response