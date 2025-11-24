from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, oauth2
from database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/")
def get_posts(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str]= ""):
    posts = db.query(models.Post).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    return  posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def create_post(post: schemas.PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    print(current_user)
    new_posts = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return  new_posts

@router.get("/{id}")
def get_posts(id: int, db: Session = Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return  post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    print(current_user)
    post_query= db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()