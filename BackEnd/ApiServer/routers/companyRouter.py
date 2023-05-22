from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from crud import companyCrud, userCrud
from database import get_db
import schemas.all_schemas as schemas

router = APIRouter(prefix='/companies', tags=['companies'])

auth_scheme = HTTPBearer()


@router.get("/", response_model=list[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = companyCrud.get_all_companies(db, skip=skip, limit=limit)
    return companies


@router.get("/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = companyCrud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.post("/create/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate,
                   db: Session = Depends(get_db),
                   token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_user = userCrud.get_user_by_token(db, token)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    if userCrud.get_employee_by_token(db, token):
        raise HTTPException(status_code=400, detail="User already in company")

    db_company = companyCrud.create_company(db=db, company=company, owner_id=db_user.user_id)

    userCrud.create_employee(
        db=db,
        company_id=db_company.company_id,
        user_id=db_user.user_id,
        job_title=company.job_title)
    return db_company


@router.post("/add_employee/", response_model=schemas.Employee)
def add_employee(company_employee: schemas.EmployeeCreate,
                 db: Session = Depends(get_db),
                 token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_company = companyCrud.get_company_by_owner_token(db, token)
    if db_company is None:
        raise HTTPException(status_code=400, detail="User is not owner of any company")
    db_user = userCrud.get_user_by_id(db, company_employee.user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    db_employee = userCrud.get_employee(db, db_user)
    if db_employee:
        raise HTTPException(status_code=400, detail="User already in company")
    db_employee = userCrud.create_employee(
        db=db,
        company_id=db_company.company_id,
        user_id=db_user.user_id,
        job_title=company_employee.job_title)
    return db_employee


@router.get("/employees/", response_model=list[schemas.Employee])
def get_employees(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_company = companyCrud.get_company_by_owner_token(db, token)
    if db_company is None:
        raise HTTPException(status_code=400, detail="User is not owner of any company")
    db_user_company_employees = companyCrud.get_all_employees(db, db_company.company_id)
    result = []
    for db_user, db_employee in db_user_company_employees:
        result.append(schemas.Employee(
            user_id=db_user.user_id,
            email=db_user.email,
            employee_id=db_employee.employee_id,
            job_title=db_employee.job_title,
            company_id=db_employee.company_id))

    return result
