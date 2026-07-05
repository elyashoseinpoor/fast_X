from database import SessionLocal , User



# CREATE
#db = SessionLocal()
#user = User(first_name="Ali",last_name="Ahmadi",email="ali@test.com",hashed_password="123")
#db.add(user)
#print("Before commit:", user.id)  
#db.commit()
#print("After commit:", user.id)  
#db.refresh(user)
#print("Refreshed ID:", user.id)
#db.close()

#multi create
#db = SessionLocal()
#users = [
#    User(first_name="A", last_name="A", email="a@test.com", hashed_password="1"),
#    User(first_name="B", last_name="B", email="b@test.com", hashed_password="2"),
#    User(first_name="C", last_name="C", email="c@test.com", hashed_password="3"),]
#db.add_all(users)
#db.commit()
#for u in users:
#    db.refresh(u)
#    print(u.id, u.email)
#db.close()


#update_object's
#db = SessionLocal()
#user = db.query(User).first()
#print("Original:", user.first_name)
#user.first_name = "Changed"
#print("Changed in Python (NOT DB yet):", user.first_name)
#db.commit()
#print("Now saved to DB")
#db.close()

#rollback
#db = SessionLocal()
#user = User(first_name="Temp",last_name="User",email="temp@test.com",hashed_password="123")
#db.add(user)
#print("Before rollback:", user.email)
## این user اصلاً وارد DB نمی‌شود
#db.commit()
#db.close()

#dirty
db = SessionLocal()
user = db.query(User).first()
print("Is dirty before change?")
user.first_name = "X"
print(db.dirty)  # 👈 خیلی مهم
db.commit()
db.close()