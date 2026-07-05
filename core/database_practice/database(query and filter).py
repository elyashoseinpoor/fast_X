from database import SessionLocal, User, Order
from sqlalchemy import func

db = SessionLocal()


# ---------------------------
# SIMPLE FILTER
# ---------------------------
ali = db.query(User).filter(User.first_name == "Ali").first()
if ali:
    print("Find Ali:", ali.email)


# ---------------------------
# FILTER WITH CONDITION
# ---------------------------
users = db.query(User).filter(User.id > 0).all()
print("Users count:", len(users))


# ---------------------------
# LIKE SEARCH
# ---------------------------
users = db.query(User).filter(User.email.like("%test%")).all()

for u in users:
    print("LIKE:", u.email)


# ---------------------------
# GET RELATIONSHIP DATA
# ---------------------------
user = db.query(User).filter(User.first_name == "Ali").first()

if user:
    for o in user.orders:
        print("ORDER:", o.title)


# ---------------------------
# JOIN QUERY
# ---------------------------
results = db.query(User, Order).join(Order).all()

for u, o in results:
    print("JOIN:", u.first_name, "->", o.title)


# ---------------------------
# AGGREGATION (COUNT)
# ---------------------------
result = db.query(
    User.first_name,
    func.count(Order.id)
).join(Order).group_by(User.id).all()

for name, count in result:
    print("COUNT:", name, count)


# ---------------------------
# USERS WITHOUT ORDERS
# ---------------------------
no_orders = db.query(User).outerjoin(Order).filter(Order.id == None).all()

for u in no_orders:
    print("NO ORDER:", u.first_name)


# ---------------------------
# DELETE EXAMPLE
# ---------------------------
u = db.query(User).filter(User.first_name == "Sara").first()

if u:
    db.delete(u)
    db.commit()


db.close()