from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.database.base import Base

class Task(Base):
    __tablename__ = "tasks"

    # Define columns for the tasks table
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    due_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)