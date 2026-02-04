from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import init_db, session
from app.services import tasks_service, users_service
from app.schemas import tasks_schema, users_schema
from app.models import tasks as tasks_model, users as user_models

init_db._init_db()
app = FastAPI(title="Task Service API")

def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to the Task Service API"}

#CRUD for Users

#Create User
@app.post("/users/", response_model=users_schema.User)
def create_user(user: users_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = users_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_service.create_user(db=db, user=user)

#Read all users
@app.get("/users", response_model=list[users_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = users_service.get_users(db, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

#Read User by ID
@app.get("/users/{user_id}", response_model=users_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


#CRUD for Tasks

#Create Task
@app.post("/users/{user_id}/tasks/", response_model=tasks_schema.Task)
def create_task_for_user(user_id: int, task: tasks_schema.TaskCreate, db: Session = Depends(get_db)):
    db_user = users_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return tasks_service.create_task(db=db, task=task, owner_id=user_id)

#Read all Tasks with pagination
@app.get("/tasks/", response_model=list[tasks_schema.Task])
def read_tasks(skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    tasks = tasks_service.get_tasks(db, skip=skip, limit=limit)
    return tasks

#Upgrade Task
@app.put("/tasks/{task_id}", response_model=tasks_schema.Task)
def update_task(task_id: int, task: tasks_schema.TaskCreate, is_completed: bool, db: Session = Depends(get_db)):
    db_task = tasks_service.update_task(db, task_id=task_id, is_completed=is_completed)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

#Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = tasks_service.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}