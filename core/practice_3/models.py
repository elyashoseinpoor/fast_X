from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    email = Column(String)
    expenses = relationship("Expense", back_populates="person")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(String)
    amount = Column(Integer)
    description = Column(String)

    person_id = Column(Integer, ForeignKey("persons.id"))
    person = relationship("Person", back_populates="expenses")
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    expenses = relationship("Expense", back_populates="category")