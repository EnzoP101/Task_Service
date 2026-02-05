from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from schemas.tasks_schema import Task

#Schema for Users

# Base schema for User
class UserBase(BaseModel):
    email: EmailStr

# Schema for creating a User
class UserCreate(UserBase):
    password: str
    username: str

# Schema for User
class User(UserBase):
    id: int
    is_active: bool
    role: str
    created_at: datetime

    class Config:
        orm_mode = True
