from sqlmodel import SQLModel, create_engine
import os

SQLLITE_FILE_NAME = "_app.db"
DB_FOLDER = "backend/db/"
SQLLITE_URL = f"sqlite:///{os.path.join(DB_FOLDER, SQLLITE_FILE_NAME)}"

connect_args = {"check_same_thread": False}
engine = create_engine(SQLLITE_URL, echo=True, connect_args=connect_args)

def create_db_and_tables():
	SQLModel.metadata.create_all(engine)