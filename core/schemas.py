from pydantic import BaseModel, field_validator


class items_create(BaseModel):
    name: str
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        if value.lower() == "admin":
            raise ValueError("Invalid name")
        if len(value) < 3:
            raise ValueError("please take with 3 char!")
        return value


class items_response(items_create):
    id: int


class items_edit(items_create):
    pass