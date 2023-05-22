from sqlalchemy import and_
from sqlalchemy.orm import Session

from crud import userCrud
from models import companyModel, employeeModel, userModel
from schemas import companySchema


def get_company(db: Session, company_id: int):
    return db.query(companyModel.Company).filter(companyModel.Company.company_id == company_id).first()


def create_company(db: Session, company: companySchema.CompanyCreate, owner_id):
    db_company = companyModel.Company(
        owner_id=owner_id,
        TIN=company.TIN,
        name=company.name,
        legal_name=company.legal_name,
        phone_number=company.phone_number,
        description=company.description
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def employee_exists(db: Session, company_id: int, user_id: int):
    return db.query(employeeModel.Employee).filter(
        and_(employeeModel.Employee.company_id == company_id,
             employeeModel.Employee.user_id == user_id)
    ).first() is not None


def get_all_employees(db: Session, company_id: int):
    db_employee = db.query(userModel.User, employeeModel.Employee).filter(
        and_(userModel.User.user_id == employeeModel.Employee.user_id,
             employeeModel.Employee.company_id == company_id)).all()
    print(db_employee)
    return db_employee


def add_employee(db: Session, company_id: int, user_id: int, job_title: str):
    db_employee = employeeModel.Employee(company_id=company_id, user_id=user_id, job_title=job_title)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_platforms(db: Session, company_id: int):
    return db.query(companyModel.Company).filter(companyModel.Company.company_id == company_id).first().platforms


def get_company_by_employee(db: Session, employee_id: int):
    return db.query(companyModel.Company).join(employeeModel.Employee).filter(
        employeeModel.Employee.user_id == employee_id).first()


def get_company_by_owner_token(db: Session, token: str):
    db_user = userCrud.get_user_by_token(db, token)
    if db_user is None:
        return None
    user_id = db_user.user_id
    db_company = db.query(companyModel.Company).filter(companyModel.Company.owner_id == user_id).first()
    return db_company


def get_all_companies(db, skip, limit):
    return db.query(companyModel.Company).offset(skip).limit(limit).all()
