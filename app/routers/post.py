from .. import models, schemas, utils
from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from starlette import status
import psycopg2

router = APIRouter(
<<<<<<< HEAD
    prefix="/posts"
=======
    prefix="/posts",
    tags=['Posts']
>>>>>>> d2683bf (Sean Sep 8)
)

@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts


# change the default status code
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING *"""
                   # , (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()  # save changes to the DB

    new_posts = models.Post(title=post.title, content=post.content, published=post.published)
    # or replace with **post.dict() -> new_posts = models.Post(**post.dict())

    db.add(new_posts)
    db.commit()
    db.refresh(new_posts) # not a dictionary yet

    return new_posts


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", str(id))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    return post


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", str(id))
    # deleted_post = cursor.fetchone()

    # conn.commit()

    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the {id} doesn't exist")

    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   # (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the {id} doesn't exist")

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()