import datetime
from backend.db.models import RPN
from backend.db.database import engine
from sqlmodel import Session

#It supposes that token are splitted by spaces
async def evaluate_rpn(expression):
	calc = []
	
	operators = {'+': lambda x, y: x + y,
				 '-': lambda x, y: x - y,
				 '*': lambda x, y: x * y,
				 '/': lambda x, y: x / y,
				 '^': lambda x, y: x ** y,
				 '%': lambda x, y: x % y}

	expressionStr = expression
	expression = expression.split()

	if len(expression) % 2 == 0:
		raise ValueError("Invalid expression")
	
	for token in expression:
		if token.isdigit():
			calc.append(int(token))
		elif token in operators:
			if len(calc) < 2:
				raise ValueError("Invalid expression")
			operand2 = calc.pop()
			operand1 = calc.pop()
			result = operators[token](operand1, operand2)
			calc.append(result)
		else:
			raise ValueError("Invalid token: " + token)

	if len(calc) == 1:
		with Session(engine) as session:
			rpn = RPN(expression=expressionStr, result=float(calc[0]), created_at=datetime.datetime.now())
			session.add(rpn)
			session.commit()
			session.refresh(rpn)

	return calc[0]