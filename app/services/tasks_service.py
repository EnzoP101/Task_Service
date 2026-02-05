from sqlalchemy.orm import Session
from schemas import tasks_schema
from models import tasks as tasks_model
from fastapi import HTTPException

# Service functions for Tasks

# Read Operations

#Get tasks with pagination max 25 tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 25):
    return db.query(tasks_model.Task).offset(skip).limit(limit).all()

#Create Operation

def create_task(db: Session, task: tasks_schema.TaskCreate, owner_id: int):
    db_task = tasks_model.Task(**task.dict(), owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#Update Operation

def update_task(db: Session, task_id: int, task_update: tasks_schema.TaskUpdate):
    task = db.query(tasks_model.Task).filter(tasks_model.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

#Delete Operation

def delete_task(db: Session, task_id: int):
    task = db.query(tasks_model.Task).filter(tasks_model.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    raise HTTPException(status_code=200, detail="Task deleted successfully")