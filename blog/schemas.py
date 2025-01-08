from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class BlogCreate(BaseModel):
    title: str
    body: str

class Blogs(BlogCreate):
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    user_name: str
    blogs: Optional[List[Blogs]]
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config:
        orm_mode = True


class Role (str, Enum):
    admin = "admin"
    user =  "user"


class User(BaseModel):
    id: Optional[int]
    FirstName: str = Field(..., min_length=3, max_length=50, description="User's first name")
    LastName: str = Field(..., min_length=3, max_length=50, description="User's last name")
    UserName: str = Field(..., min_length=5, max_length=50, description="Username for the user")
    Email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, max_length=128, description="User's password")
    roles: List[Role]


class UserUpdateRequest (BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]

class Login(BaseModel):
    user_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_name: str | None = None
