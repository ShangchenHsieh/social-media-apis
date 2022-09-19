from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0702@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# dependency
# responsible for talking to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
    # try:
        # conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0702',
                                # cursor_factory=RealDictCursor)
        # cursor = conn.cursor()
        # print("Database connection was successful!")
        # break
    # except Exception as error:
        # print("Connecting to database failed")
        # print("Error: ", error)
