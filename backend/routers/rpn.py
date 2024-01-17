from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from backend.internal.RPN import evaluate_rpn

from backend.db.models import RPN
from backend.db.database import engine
from sqlmodel import Session, select

import pandas as pd
import io

router = APIRouter(
	prefix="/rpn",
	tags=["rpn"],
)

class Expression(BaseModel):
	expression: str

@router.post("/")
async def calcRPN(expression: Expression):
    return {"result": await evaluate_rpn(expression.expression)}


@router.get("/history", response_class=StreamingResponse)
def history():
	with Session(engine) as session:
		history = session.exec(select(RPN).order_by(RPN.created_at.desc())).all()
		
		data = pd.DataFrame([{"expression":rpn.expression,"result":rpn.result, "created_at": rpn.created_at} for rpn in history])
		
		stream = io.StringIO()
		
		data.to_csv(stream, index=False)
		
		response = StreamingResponse(iter([stream.getvalue()]),media_type="text/csv")
		response.headers["Content-Disposition"] = "attachment; filename=data.csv"
		return response