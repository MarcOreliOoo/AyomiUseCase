import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str = Field(index=True)
	secret_name: str
	age: Optional[int] = Field(default=None, index=True)


class RPN(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	expression: str
	result: float
	created_at: datetime.datetime = Field(default=None)
