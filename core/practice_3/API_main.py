from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, get_db
from models import Person, Expense, Category
from fastapi import FastAPI, Depends,status
import json
import colorama
from schemas import CreatePerson,PersonResponse,CreateExpense,ExpenseResponse,CreateCategory,CategoryResponse

colorama.init()
app = FastAPI()

#with open("person_employees.json", "r", encoding="utf-8") as file:
#    persons = json.load(file)
#@app.post("/employ_person_to_database")
#def post_persons(db: Session = Depends(get_db)):
#    for item in persons:
#        new_person = Person(
#            first_name=item["first_name"],
#            last_name=item["last_name"],
#            phone_number=item["phone_number"],
#            address=item["address"],
#            email=item["email"])
#        db.add(new_person)
#    db.commit()
#    return {"message": "50 persons inserted successfully"}

#seed-categories
#@app.post("/seed-categories")
#def seed_categories(db: Session = Depends(get_db)):
#    categories = [
#        {"id": 100, "name": "Electronics"},
#        {"id": 200, "name": "Software & IT"},
#        {"id": 300, "name": "Hardware Tools"},
#        {"id": 345, "name": "Network Devices (MikroTik / Cisco / Router)"},
#        {"id": 400, "name": "Personal Purchases"},
#        {"id": 500, "name": "Office Equipment"},
#        {"id": 600, "name": "Security & Surveillance"},
#    ]
#    for cat in categories:
#       exists = db.query(Category).filter(Category.id == cat["id"]).first()
#        if not exists:
#            new_category = Category(**cat)
#            db.add(new_category)
#    db.commit()
#    return {"message": "Categories inserted successfully"}


################################ !!! crud !!! ###################################


#creat
@app.post("/expenses",status_code=status.HTTP_201_CREATED,response_model=ExpenseResponse)
def post_data(expense: CreateExpense,db: Session = Depends(get_db)):
    new_expense = Expense(
        date=expense.date,
        amount=expense.amount,
        description=expense.description,
        person_id=expense.person_id,
        category_id=expense.category_id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.post("/persons",status_code=status.HTTP_201_CREATED,response_model=PersonResponse)
def post_data(person: CreatePerson,db: Session = Depends(get_db)):
    new_person = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        phone_number=person.phone_number,
        address=person.address,
        email=person.email
    )
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


#read
@app.get("/reading_person_database", status_code=status.HTTP_200_OK)
def get_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()

@app.get("/reading_expense_database", status_code=status.HTTP_200_OK)
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()

@app.get("/reading_category_database", status_code=status.HTTP_200_OK)
def get_categoris(db: Session = Depends(get_db)):
    return db.query(Category).all()


#update
@app.put("/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def update_expense(expense_id: int,expense: CreateExpense,db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        return {"message": "Expense not found"}
    db_expense.date = expense.date
    db_expense.amount = expense.amount
    db_expense.description = expense.description
    db_expense.person_id = expense.person_id
    db_expense.category_id = expense.category_id
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.put("/persons/{person_id}", status_code=status.HTTP_200_OK)
def update_person(person_id: int,person: CreatePerson,db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if not db_person:
        return {"message": "Person not found"}
    db_person.first_name = person.first_name
    db_person.last_name = person.last_name
    db_person.phone_number = person.phone_number
    db_person.address = person.address
    db_person.email = person.email
    db.commit()
    db.refresh(db_person)
    return db_person


#delete
@app.delete("/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def delete_expense(expense_id: int,db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        return {"message": "Expense not found"}
    db.delete(db_expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

@app.delete("/persons/{person_id}", status_code=status.HTTP_200_OK)
def delete_person(person_id: int,db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if not db_person:
        return {"message": "Person not found"}
    db.delete(db_person)
    db.commit()
    return {"message": "Person deleted successfully"}