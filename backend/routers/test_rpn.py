import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from backend.internal.RPN import evaluate_rpn
from backend.routers.rpn import router


class TestRPN(unittest.TestCase):
	def setUp(self):
		self.app = FastAPI()
		self.app.include_router(router)
		self.client = TestClient(self.app)

	async def test_calcRPN(self):
		response = self.client.post("/rpn/", json={"expression": "2 3 +"})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), {"result": await evaluate_rpn("2 3 +")})

if __name__ == '__main__':
	unittest.main()
