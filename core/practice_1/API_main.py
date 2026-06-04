from fastapi import FastAPI
from data import expenses

app = FastAPI()

@app.get("/expenses")
async def get_expenses():
    return expenses