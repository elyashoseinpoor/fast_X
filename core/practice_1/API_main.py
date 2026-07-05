#Lib's
from fastapi import FastAPI,Path,HTTPException,status
from data import expenses
from fastapi.responses import JSONResponse
import colorama

#object's
colorama.init()
app = FastAPI()

#get_for_all_expenses
@app.get("/expenses")
async def get_expenses():
    return expenses

#get_with_input_id
@app.get("/expenses/{item_id}")
def get_with_id(item_id: int = Path()):
    for name in expenses:
        if name["id"] == item_id:
            return name
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                        detail="Name not found"
                        )


#post_for_create_new_expens
@app.post("/expenses", status_code=status.HTTP_201_CREATED)
def post_data(description: str, amount: float):
    new_expense = {
        "id": max(item["id"] for item in expenses) + 1,
        "description": description,
        "amount": amount}
    expenses.append(new_expense)
    return JSONResponse(content={"message": "posted _ ok !"},
                        status_code=status.HTTP_200_OK
                       )


#put_for_edit_expenses
@app.put("/expenses/{item_id}")
async def edit_expenses(item_id: int, amount: int, description: str):
    for item in expenses:
        if item["id"] == item_id:
            item["amount"] = amount
            item["description"] = description
            return JSONResponse(content={"message": "edited _ ok !"},
                                status_code=status.HTTP_200_OK
                               )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Expense not found"
                       )


@app.delete("/expenses/{item_id}")
def names_delete(item_id: int):
    for item in expenses:
        if item["id"] == item_id:
            expenses.remove(item)
            return JSONResponse(content={"message": "deleted successfully _ ok !"},
                                status_code=status.HTTP_204_NO_CONTENT
                                )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Name not found"
                        )