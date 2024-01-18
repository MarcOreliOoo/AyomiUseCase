from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.db.database import create_db_and_tables
from backend.routers import rpn

app = FastAPI()

# Enable CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

# Include Routers
app.include_router(rpn.router)

# On startup create db and tables if needed
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
# Health check
@app.get("/health", include_in_schema=False)
def read_root():
    return {"Hello": "WORLD"}