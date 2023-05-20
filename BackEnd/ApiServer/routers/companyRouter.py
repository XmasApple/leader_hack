from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from crud import companyCrud, userCrud
from database import get_db
from schemas import companySchema, companyEmployeeSchema

router = APIRouter(prefix='/companies')

auth_scheme = HTTPBearer()


@router.get("/{company_id}", response_model=companySchema.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = companyCrud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.post("/create/", response_model=companySchema.Company)
def create_company(company: companySchema.CompanyCreate,
                   db: Session = Depends(get_db),
                   token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    if not userCrud.check_token(db, token):
        raise HTTPException(status_code=400, detail="Incorrect token")
    if userCrud.get_employee_by_token(db, token):
        raise HTTPException(status_code=400, detail="User already in company")

    db_company = companyCrud.create_company(db=db, company=company)
    db_employee = userCrud.create_employee(
        db=db,
        company_id=db_company.id,
        user_id=userCrud.get_user_by_token(db, token).id,
        job_title=company.job_title)
    return db_company


@router.post("/add_employee/", response_model=companyEmployeeSchema.CompanyEmployee)
def add_employee(company_employee: companyEmployeeSchema.CompanyEmployeeCreate,
                 db: Session = Depends(get_db),
                 token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_company = companyCrud.get_company_by_owner_token(db, token)
    if db_company is None:
        raise HTTPException(status_code=400, detail="User is not owner of any company")
    db_user = userCrud.get_user_by_id(db, company_employee.user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    if userCrud.get_employee(db, db_user.id):
        raise HTTPException(status_code=400, detail="User already in company")
    db_employee = userCrud.create_employee(
        db=db,
        company_id=db_company.id,
        user_id=db_user.id,
        job_title=company_employee.job_title)
    return db_employee


@router.get("/employees/", response_model=list[companyEmployeeSchema.CompanyEmployee])
def get_employees(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_company = companyCrud.get_company_by_owner_token(db, token)
    if db_company is None:
        raise HTTPException(status_code=400, detail="User is not owner of any company")
    return companyCrud.get_all_employees(db, db_company.id)
