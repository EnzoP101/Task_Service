from sqlalchemy.orm import Session
from schemas import users_schema
from models import users as user_models
from fastapi import HTTPException
from passlib.hash import sha256_crypt

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
    
    hashed_password = sha256_crypt.hash(user.password)
    
    db_user = user_models.User(email=user.email, username=user.username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Update Operations

#Ban User
def ban_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    elif not db_user.is_active:
        raise HTTPException(status_code=400, detail="User is already banned")
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return db_user

#Reactivate User
def reactivate_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    elif db_user.is_active:
        raise HTTPException(status_code=400, detail="User is already active")
    db_user.is_active = True
    db.commit()
    db.refresh(db_user)
    return db_user
