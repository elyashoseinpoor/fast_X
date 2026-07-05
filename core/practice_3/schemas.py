from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict
from datetime import date
import re
from typing import Optional


# ---------------- Person ----------------

class CreatePerson(BaseModel):
    first_name: str = Field(min_length=2, max_length=30)
    last_name: str = Field(min_length=2, max_length=30)
    phone_number: str
    address: str = Field(min_length=5, max_length=100)
    email: EmailStr

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Value cannot be empty.")
        if not re.fullmatch(r"^[A-Za-zآ-ی\s]+$", value):
            raise ValueError("Only letters are allowed.")
        return value
    
    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, value: str):
        if not re.fullmatch(r"^09\d{9}$", value):
            raise ValueError("Invalid phone number.")
        return value

class PersonResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    address: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


# ---------------- Expense ----------------

class CreateExpense(BaseModel):
    date: date
    description: str = Field(min_length=5, max_length=70)
    amount: float = Field(gt=0)
    person_id: int = Field(ge=1, le=9999)
    category_id: int = Field(ge=1, le=9999)
    
    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Description cannot be empty.")
        return value

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: float):
        if round(value, 2) != value:
            raise ValueError("Maximum 2 decimal places.")
        return value


class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float
    model_config = ConfigDict(from_attributes=True)


# ---------------- Category ----------------

class CreateCategory(BaseModel):
    name: str = Field(min_length=2, max_length=40)

class CategoryResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

# ---------------- Update ----------------

class UpdateExpense(BaseModel):
    description: Optional[str] = None
    amount: Optional[float] = None


class UpdatePerson(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None

class UpdateCategory(BaseModel):
    name: Optional[str] = None