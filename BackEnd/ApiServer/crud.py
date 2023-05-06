import hashlib

from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    # use sha256 to hash password
    h = hashlib.sha256()
    h.update(user.password.encode('utf-8'))
    hashed_password = h.hexdigest()

    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_password(db: Session, user: schemas.UserCreate):
    db_user = get_user_by_email(db, user.email)

    if db_user:
        h = hashlib.sha256()
        h.update(user.password.encode('utf-8'))
        hashed_password = h.hexdigest()
        return db_user.hashed_password == hashed_password
    return False


def get_user_id_by_email(db: Session, email: str):
    db_user = get_user_by_email(db, email)
    if db_user:
        return db_user.id
    return None


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()