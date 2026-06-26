#Lib's
from fastapi import FastAPI,Path,HTTPException,status
import json
from fastapi.responses import JSONResponse
import colorama
from schemas import CreateExpense,ExpenseResponse

#json_load
with open("data.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

#object's
colorama.init()
app = FastAPI()

#get_for_all_expenses
@app.get("/expenses")
async def get_expenses():
    return expenses

#get_with_input_id
@app.get("/expenses/{item_id}",status_code=status.HTTP_200_OK,response_model=ExpenseResponse)
def get_with_id(item_id: int = Path(gt=0, description="Expense ID")):
    for expense in expenses:
        if expense["id"] == item_id:
            return expense
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Expense not found")


#post_for_create_new_expens
@app.post("/expenses", status_code=status.HTTP_201_CREATED,response_model=ExpenseResponse)
def post_data(expense: CreateExpense):
    new_expense = {
        "id": max(item["id"] for item in expenses) + 1,
        "description": expense.description,
        "amount": expense.amount}
    expenses.append(new_expense)
    print(expense.model_dump()) 
    return new_expense


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