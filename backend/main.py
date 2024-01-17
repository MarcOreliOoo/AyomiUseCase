#python -m uvicorn backend.main:app --reload
from fastapi import FastAPI
from backend.db.database import create_db_and_tables
""" from sqlmodel import Session, select
from backend.db.models import Hero
from backend.db.database import engine """


from backend.routers import rpn

app = FastAPI()
app.include_router(rpn.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/health", include_in_schema=False)
def read_root():
    return {"Hello": "WORLD"}


""" @app.post("/heroes/")
def create_hero(hero: Hero):
	with Session(engine) as session:
		session.add(hero)
		session.commit()
		session.refresh(hero)
		return hero


@app.get("/heroes/")
def read_heroes():
	with Session(engine) as session:
		heroes = session.exec(select(Hero)).all()
		return heroes """