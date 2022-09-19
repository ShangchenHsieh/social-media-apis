import psycopg2
from fastapi import FastAPI, Response, HTTPException, Depends
from psycopg2.extras import RealDictCursor
from pydantic import BaseSettings
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import post, user, auth


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "postgres"
    secret_key: str = ""


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"Message": "Welcome to my page"}
