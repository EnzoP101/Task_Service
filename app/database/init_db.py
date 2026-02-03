from app.database.session import engine
from app.database.base import Base
from app.models.users import User, Task

def init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)