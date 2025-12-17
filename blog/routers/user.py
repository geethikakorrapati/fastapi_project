from fastapi import APIRouter,Depends,status,HTTPException
from .. import database,schemas,models
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash
from ..repository import user
get_db=database.get_db




router= APIRouter(prefix="/user",tags=["Users"])

@router.post('/', response_model=schemas.showUserout)
def create_user(request: schemas.Userout, db: Session = Depends(database.get_db)):
    return user.create(request,db)


@router.get('/{id}', response_model=schemas.showUserout)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id,db)
