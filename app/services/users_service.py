from sqlalchemy.orm import Session
from schemas import users_schema
from models import users as user_models
from fastapi import HTTPException

# Service functions for Users

#Read Operations
def get_user(db: Session, user_id: int):
    user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(user_models.User).filter(user_models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).offset(skip).limit(limit).all()
#Create Operation

def create_user(db: Session, user: users_schema.UserCreate):
    
    hashed_password = user.password + "notreallyhashed"
    
    db_user = user_models.User(email=user.email, username=user.username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user