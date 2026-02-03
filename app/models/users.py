from app.database.base import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

class User(Base):
    __tableName__ = "users"

    #Define columns for the users table
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(45), unique=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), nullable=False, default="user")
    created_at = Column(DateTime, nullable=False)