from .database import SessionLocal, engine
from .models import User
from sqlalchemy.exc import IntegrityError

# Create tables
User.metadata.create_all(bind=engine)

def add_userdata(user_dict: dict):
    db = SessionLocal()
    try:
        db_user = User(**user_dict)
        db.add(db_user)
        db.commit()
    except IntegrityError:
        db.rollback()
    finally:
        db.close()

def read_usersdata():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"data": [{"id": u.id, "name": u.name, "email": u.email} for u in users]}

