from .. import models, schemas, utils
from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from starlette import status
import psycopg2

router = APIRouter(
<<<<<<< HEAD
    prefix="/users"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def created_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

=======
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def created_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
>>>>>>> d2683bf (Sean Sep 8)
    # hash the pw - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
<<<<<<< HEAD
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with id {id} does not exist")
    return user

=======
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    return user
>>>>>>> d2683bf (Sean Sep 8)
