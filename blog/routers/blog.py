from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, database, models,oauth2
from ..hashing import Hash   # make sure hashing file exists
from ..repository import blog


router = APIRouter(prefix="/blog",tags=["Blogs"])



@router.get('/', response_model=List[schemas.showBlog])
def all(db: Session = Depends(database.get_db),current_user:schemas.Userout =Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.Userout =Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}', response_model=schemas.showBlog)
def show(id: int, db: Session = Depends(database.get_db),current_user:schemas.Userout =Depends(oauth2.get_current_user)):
    return blog.show(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.Userout =Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db),current_user:schemas.Userout =Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)


