from app.database.session import engine
from app.database.base import Base
from app.models.users import User
from app.models.tasks import Task

def _init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)