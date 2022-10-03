import psycopg2
from fastapi import FastAPI, Response, HTTPException, Depends
from psycopg2.extras import RealDictCursor
from pydantic import BaseSettings
from starlette.middleware.cors import CORSMiddleware

from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"Message": "Welcome to my page"}
