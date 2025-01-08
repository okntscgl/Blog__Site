from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=False)
    user_name = Column(String, ForeignKey("users.user_name"))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    isActive = Column(Boolean, default=True)

    blogs = relationship("Blog", back_populates="creator")
