from fastapi import FastAPI
from api.books import router as books_router
from db.database import engine
from db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books_router)