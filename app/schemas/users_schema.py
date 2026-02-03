from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from app.schemas.tasks_schema import Task

#Schema for Users

# Base schema for User
class UserBase(BaseModel):
    email: EmailStr

# Schema for creating a User
class UserCreate(UserBase):
    password: str

# Schema for User
class User(UserBase):
    id: int
    username: str
    is_active: bool
    role: str
    created_at: datetime
    tasks: List['Task'] = []

    class Config:
        orm_mode = True