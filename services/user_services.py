from sqlalchemy.orm import Session
from models.user_models import User
from schemas import user


def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_cpf(db: Session, cpf: str):
    return db.query(User).filter(User.cpf == cpf).first()

def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user.UserCreate):
    user_db = User(**user.dict()) # **user.dict()
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
