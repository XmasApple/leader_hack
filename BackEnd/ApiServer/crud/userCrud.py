import secrets
import hashlib
import time

from sqlalchemy.orm import Session
from models import userModel, userTokenModel, companyEmployeeModel
from schemas import userSchema


def get_user_by_id(db: Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(userModel.User).filter(userModel.User.email == email).first()


def create_user(db: Session, user: userSchema.UserAuth):
    # use sha256 to hash password
    h = hashlib.sha256()
    h.update(user.password.encode('utf-8'))
    hashed_password = h.hexdigest()

    db_user = userModel.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_password(db: Session, user: userSchema.UserAuth):
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
    return db.query(userModel.User).offset(skip).limit(limit).all()


def create_token(db: Session, user_id: int, life_time: int = 0):
    if life_time == 0:
        life_time = 3600 * 24 * 7
    # generate random token
    token = secrets.token_hex(32)
    db_token = userTokenModel.UserToken(token=token, user_id=user_id, expire_date=time.time() + life_time)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def check_token(db: Session, token: str):
    print(token)
    db_token = db.query(userTokenModel.UserToken).filter(userTokenModel.UserToken.token == token).first()
    if not db_token:
        return False
    if db_token.expire_date <= time.time():
        db.delete(db_token)
        db.commit()
    else:
        return True


def get_user_by_token(db: Session, token: str):
    db_token = db.query(userTokenModel.UserToken).filter(userTokenModel.UserToken.token == token).first()
    if db_token:
        return db.query(userModel.User).filter(userModel.User.id == db_token.user_id).first()
    return None


def check_user_is_company_employee(db: Session, user_id: int):
    return db.query(userModel.CompanyEmployee).filter(userModel.CompanyEmployee.user_id == user_id).first() is not None


def get_employee(db: Session, user: userModel.User):
    return db.query(userModel.User, companyEmployeeModel.CompanyEmployee).filter(
        user.id == companyEmployeeModel.CompanyEmployee.user_id).first()


def get_employee_by_token(db: Session, token: str):
    db_token = db.query(userTokenModel.UserToken).filter(userTokenModel.UserToken.token == token).first()
    if db_token:
        return get_employee(db, get_user_by_id(db, db_token.user_id))
    return None


def create_employee(db: Session, user_id: int, company_id: int, job_title: str):
    db_employee = companyEmployeeModel.CompanyEmployee(user_id=user_id, company_id=company_id, job_title=job_title)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
