from fastapi import APIRouter,Depends,status,HTTPException
from .. import database,schemas,models
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash
from ..repository import user
get_db=database.get_db

def create(request: schemas.Userout,db:Session):
    new_user = models.Userout(
        name=request.name,
        email=request.email,
        password=Hash.argon2(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id :int,db:Session):
    user = db.query(models.Userout).filter(models.Userout.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user