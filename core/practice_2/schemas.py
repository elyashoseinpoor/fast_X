from pydantic import BaseModel,field_validator,Field
import re

class CreateExpense(BaseModel):
        description: str = Field(min_length=5, max_length=70)
        amount: float = Field(gt=0, le=10000)
        
        @field_validator("description")
        @classmethod
        def description_validator(cls,value :str):
            value = value.strip()
            if not value:
                raise ValueError("Name cannot be empty")
            if not re.fullmatch(r"^[آ-ی\s‌]+$", value):
                raise ValueError("Only Persian letters and spaces are allowed.")
            return value
        
        @field_validator("amount")
        @classmethod
        def amount_validator(cls,value :float):
            if round(value, 2) != value:
                raise ValueError("Amount can have at most 2 decimal places.")
            return value

class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float


class update:
    pass 

class delete:
    pass