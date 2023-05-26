import secrets
import hashlib
import time

from sqlalchemy.orm import Session
import models.all_models as models
import schemas.all_schemas as schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserAuth):
    # use sha256 to hash password
    h = hashlib.sha256()
    h.update(user.password.encode('utf-8'))
    hashed_password = h.hexdigest()

    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_password(db: Session, user: schemas.UserAuth):
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
        return db_user.user_id
    return None


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_token(db: Session, user_id: int, life_time: int = 0):
    if life_time == 0:
        life_time = 3600 * 24 * 7
    token = secrets.token_hex(32)
    db_token = models.Token(token=token, user_id=user_id, expire_date=time.time() + life_time)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def check_token(db: Session, token: str):
    db_token = db.query(models.Token).filter(models.Token.token == token).first()
    if not db_token:
        return False
    if db_token.expire_date <= time.time():
        db.delete(db_token)
        db.commit()
    else:
        return True


def get_user_by_token(db: Session, token: str):
    db_token = db.query(models.Token).filter(models.Token.token == token).first()
    if db_token:
        return db.query(models.User).filter(models.User.user_id == db_token.user_id).first()
    return None


def check_user_is_company_employee(db: Session, user_id: int):
    return db.query(models.CompanyEmployee).filter(models.CompanyEmployee.user_id == user_id).first() is not None


def get_employee(db: Session, user: models.User):
    return db.query(models.Employee).filter(models.Employee.user_id == user.user_id).first()


def get_employee_by_token(db: Session, token: str):
    db_token = db.query(models.Token).filter(models.Token.token == token).first()
    if db_token:
        return get_employee(db, get_user_by_id(db, db_token.user_id))
    return None


def create_employee(db: Session, user_id: int, company_id: int, job_title: str):
    db_employee = models.Employee(
        user_id=user_id,
        company_id=company_id,
        job_title=job_title)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
