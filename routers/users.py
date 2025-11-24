from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import models, schemas, utils
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", response_model=schemas.UserOut)
def create_User(user: schemas.UserCreate, db: Session = Depends(get_db),):

    # hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_users = models.User(**user.model_dump())
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return  new_users