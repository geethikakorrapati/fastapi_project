from fastapi import FastAPI
from .import models
from . database import engine
from .routers import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()"""

#@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
#def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#    db.add(new_blog)
#    db.commit()
#    db.refresh(new_blog)
#    return new_blog

#@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
#def destroy(id,db: Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return{'done'}

#@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
#def update(id,request:schemas.Blog,db: Session = Depends(get_db)):
#    blog=db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#    blog.update(request.dict())
#    db.commit()
#    return 'updated successfully'




#@app.get('/blog/{id}',status_code=200,response_model=schemas.showBlog,tags=['blogs'])
#def show(id: int, response:Response,db:Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#    if not blog:
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog with the id {id} is not available")
#       #response.status_code =status.HTTP_404_NOT_FOUND
#       #return{'detail':f"Blog with the id {id} is not available"}
#    return blog




#@app.post('/user',response_model=schemas.showUserout,tags=['Users'])
#def create_user(request: schemas.Userout,db: Session = Depends(get_db)):
    
#    new_user=models.Userout(name=request.name,email=request.email,password= Hash.argon2(request.password))
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#    return new_user

#@app.get('/user/{id}',response_model=schemas.showUserout,tags=['Users'])
#def get_user(id:int,db: Session = Depends(get_db)):
#    user = db.query(models.Userout).filter(models.Userout.id == id).first()
#    if not user :
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Userid with the id {id} is not available")
#        #response.status_code =status.HTTP_404_NOT_FOUND
#        #return{'detail':f"Blog with the id {id} is not available"}
#    return user