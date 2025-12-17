from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit: int=10,published: bool=True,sort: Optional[str] = None):
    # only to get 10 published blogs
    if published:
        return {'message': f"{limit} blogs from the data base is {published} and {sort}"}
    else:
        return {'message': f"{limit} blogs from the data base {published}"}

@app.get("/blog/unpublished")
def unpublished():
    return {'message': "all unpublished blogs" }

@app.get("/blog/{id}")
def read_root(id : int):
    return {'message': id }

@app.get("/blog/{id}")
def show(id : int):
    return {'message': id }


@app.get("/blog/{id}/comment")
def comment(id):
    return {'message': {'1','2'} }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
@app.post("/blog")
def create_blog(request: Blog):
    x=1
    return {"data":f"blog is created with title as {request.title}"}