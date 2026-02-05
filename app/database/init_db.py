from database.session import engine
from database.base import Base
from models.users import User
from models.tasks import Task

def _init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)