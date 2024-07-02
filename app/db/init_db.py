from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_class import Base
from .session import engine
import models  # Uvoz svih modela koje ste definisali

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
