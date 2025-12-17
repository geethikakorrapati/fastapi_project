from pydantic import BaseModel
from typing import List
from typing import Optional


class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    model_config = {
        "from_attributes": True
    }



class Userout(BaseModel):
    name:str
    email:str
    password:str

class showUserout(BaseModel):
    name:str
    email:str
    blogs : List[Blog]=[]
    model_config = {
        "from_attributes": True
    }

class showBlog(BaseModel):
    title:str
    body:str
    creator : showUserout
    model_config = {
        "from_attributes": True
    }

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str]= None