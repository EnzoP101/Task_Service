from app.database.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    #Define columns for the users table
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    role = Column(String(20), nullable=False, default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    tasks = relationship("Task", back_populates="owner")