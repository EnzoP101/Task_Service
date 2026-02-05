from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for Tasks

# Base schema for Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for creating a Task
class TaskCreate(TaskBase): pass

# Schema for Task Read
class Task(TaskBase):
    id: int
    user_id: int
    is_completed: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Schema for Task Update
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None