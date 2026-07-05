from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey


# data_base_info
DATABASE_URL = "sqlite:///./database.db"  
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# model's
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    title = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # رابطه
    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")


# make_data_base
print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database created successfully!")