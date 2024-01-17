from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from backend.internal.RPN import evaluate_rpn

import pandas as pd
import io

router = APIRouter(
	prefix="/rpn",
	tags=["rpn"],
)

class Expression(BaseModel):
	expression: str

@router.get("/{expression}")
async def calcRPN(expression: str):
    try: 
        return {"result": evaluate_rpn(expression)}
    except (ValueError, TypeError) as e: 
        return {"error": str(e)}

@router.post("/")
async def calcRPN(expression: Expression):
    return {"result": evaluate_rpn(expression.expression)}

@router.get("/download", response_class=StreamingResponse)
async def download():
	data = pd.DataFrame([{"expression":"1 2 +","result":"3"},{"expression":"2 3 *","result":"6"},{"expression":"2 3 + 4 *","result":"20"}])
	stream = io.StringIO()
	data.to_csv(stream, index=False)
	response = StreamingResponse(
		iter([stream.getvalue()]), media_type="text/csv")
	response.headers["Content-Disposition"] = "attachment; filename=data.csv"
	return response