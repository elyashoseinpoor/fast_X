from database import SessionLocal, Base, engine
from database import User, Order

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# create user
user = User(first_name="Ali", last_name="Ahmadi")

# create orders
order1 = Order(title="Phone")
order2 = Order(title="Laptop")

# connect relationship
user.orders = [order1, order2]

db.add(user)
db.commit()

db.refresh(user)

print(user.first_name, user.last_name)

for o in user.orders:
    print(o.title)

db.close()