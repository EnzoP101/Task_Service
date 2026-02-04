from pydantic import BaseModel
from typing import Optional

# Schema for Tasks

# Base schema for Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for creating a Task
class TaskCreate(TaskBase): pass

# Schema for Task
class Task(TaskBase):
    id: int
    owner_id: int
    is_completed: bool
    created_at: str

    class Config:
        orm_mode = True