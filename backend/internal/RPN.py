#It supposes that token are splitted by spaces
def evaluate_rpn(expression):
	calc = []
	operators = {'+': lambda x, y: x + y,
				 '-': lambda x, y: x - y,
				 '*': lambda x, y: x * y,
				 '/': lambda x, y: x / y,
				 '^': lambda x, y: x ** y,
				 '%': lambda x, y: x % y}

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

	return calc[0]


""" expression = input("Enter an expression in Reverse Polish Notation: ")
result = evaluate_rpn(expression)
print("Result:", result)
 """