from sqlalchemy import Column, Integer, String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"  # Must define table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id =Column(Integer,ForeignKey('users.id'))

    creator = relationship("Userout", back_populates="blogs")

class Userout(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    

    blogs = relationship("Blog", back_populates="creator")
