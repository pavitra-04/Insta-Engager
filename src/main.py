from fastapi import FastAPI
from src.database import engine, Base
import src.models

app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return {"message": "InstaEngager running"}
