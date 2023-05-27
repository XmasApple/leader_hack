from sqlalchemy import and_
from sqlalchemy.orm import Session

from crud import userCrud
import models.all_models as models
import schemas.all_schemas as schemas


def get_company_by_id(db: Session, company_id: int, is_verified: bool = True):
    return db.query(models.Company).filter(
        and_(
            models.Company.company_id == company_id,
            models.Company.is_verified == int(is_verified)
        )).first()


def create_company(db: Session, company: schemas.CompanyCreate, owner_id):
    db_company = models.Company(
        owner_id=owner_id,
        TIN=company.TIN,
        name=company.name,
        legal_name=company.legal_name,
        phone_number=company.phone_number,
        description=company.description,
        logo=company.logo
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def employee_exists(db: Session, company_id: int, user_id: int):
    return db.query(models.Employee).filter(
        and_(models.Employee.company_id == company_id,
             models.Employee.user_id == user_id)
    ).first() is not None


def get_all_employees(db: Session, company_id: int):
    db_employee = db.query(models.User, models.Employee).filter(
        and_(models.User.user_id == models.Employee.user_id,
             models.Employee.company_id == company_id)).all()
    return db_employee


def add_employee(db: Session, company_id: int, user_id: int, job_title: str):
    db_employee = models.Employee(company_id=company_id, user_id=user_id, job_title=job_title)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_platforms(db: Session, company_id: int):
    return db.query(models.Company).filter(
        and_(models.Company.company_id == company_id,
             models.Company.is_verified == 1
             )).first().platforms


def get_company_by_employee(db: Session, employee_id: int):
    return db.query(models.Company).join(models.Employee).filter(
        models.Employee.user_id == employee_id).first()


def get_company_by_owner_token(db: Session, token: str):
    db_user = userCrud.get_user_by_token(db, token)
    if db_user is None:
        return None
    user_id = db_user.user_id
    db_company = db.query(models.Company).filter(models.Company.owner_id == user_id).first()
    return db_company


def get_all_companies(db, skip, limit):
    return db.query(models.Company).filter(
        models.Company.is_verified == 1
    ).offset(skip).limit(limit).all()


def get_company_by_token(db: Session, token: str):
    db_query = db.query(models.Token, models.Employee, models.Company) \
        .filter(and_(models.Token.user_id == models.Employee.user_id,
                     models.Employee.company_id == models.Company.company_id,
                     models.Token.token == token,
                     models.Company.is_verified == 1
                     )).first()
    if db_query is None:
        return None
    db_token, db_employee, db_company = db_query
    return db_company


def get_platforms_by_owner_token(db: Session, token: str):
    db_company = get_company_by_owner_token(db, token)
    if db_company is None:
        return None
    db_platforms = db.query(models.Platform).filter(models.Platform.company_id == db_company.company_id).all()
    return db_platforms


def get_platform_by_owner_token(db: Session, token: str, platform_id: int):
    db_company = get_company_by_owner_token(db, token)
    if db_company is None:
        return None
    db_platform = db.query(models.Platform).filter(
        and_(models.Platform.company_id == db_company.company_id,
             models.Platform.platform_id == platform_id)).first()
    return db_platform


def get_company_by_employee_token(db: Session, token: str):
    db_user = userCrud.get_user_by_token(db, token)
    if db_user is None:
        return None
    db_employee = userCrud.get_employee(db, db_user)
    if db_employee is None:
        return None
    db_company = db.query(models.Company).filter(
        models.Company.company_id == db_employee.company_id).first()
    return db_company


def get_platform_by_employee_token(db: Session, token: str, platform_id: int):
    db_company = get_company_by_employee_token(db, token)
    if db_company is None:
        return None
    db_platform = db.query(models.Platform).filter(
        and_(models.Platform.company_id == db_company.company_id,
             models.Platform.platform_id == platform_id)).first()
    return db_platform
