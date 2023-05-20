from sqlalchemy import and_
from sqlalchemy.orm import Session

from crud import userCrud
from models import companyModel, companyEmployeeModel, userTokenModel
from schemas import companySchema


def get_company(db: Session, company_id: int):
    return db.query(companyModel.Company).filter(companyModel.Company.id == company_id).first()


def create_company(db: Session, company: companySchema.CompanyCreate):
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def employee_exists(db: Session, company_id: int, user_id: int):
    return db.query(companyEmployeeModel.CompanyEmployee).filter(
        and_(companyEmployeeModel.CompanyEmployee.company_id == company_id,
             companyEmployeeModel.CompanyEmployee.user_id == user_id)
    ).first() is not None


def get_all_employees(db: Session, company_id: int):
    return db.query(companyEmployeeModel.CompanyEmployee).filter(
        companyEmployeeModel.CompanyEmployee.company_id == company_id).all()


def add_employee(db: Session, company_id: int, user_id: int, job_title: str):
    db_employee = companyEmployeeModel.CompanyEmployee(company_id=company_id, user_id=user_id, job_title=job_title)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_platforms(db: Session, company_id: int):
    return db.query(companyModel.Company).filter(companyModel.Company.id == company_id).first().platforms


def get_company_by_employee(db: Session, employee_id: int):
    return db.query(companyModel.Company).join(companyEmployeeModel.CompanyEmployee).filter(
        companyEmployeeModel.CompanyEmployee.user_id == employee_id).first()


def get_company_by_owner_token(db: Session, token: str):
    user_id = userCrud.get_user_by_token(db, token).id
    db_company = db.query(companyModel.Company).filter(companyModel.Company.owner_id == user_id).first()
    return db_company

