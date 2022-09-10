import psycopg2
from fastapi import FastAPI, Response, HTTPException, Depends
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import post, user
from .routers import post, user, auth

# should be able to see this comment
# comments from laptop

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0702',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)


get_db()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"Message": "Welcome to my page"}





