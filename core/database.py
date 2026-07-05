from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# make_data_base
from models import User , Order
print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database created successfully!")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
