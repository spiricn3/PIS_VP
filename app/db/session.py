from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from dotenv import load_dotenv
# import os

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
# MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL="mysql+pymysql://root:@localhost/voznipark"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()