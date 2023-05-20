from pydantic import BaseModel

from models.userModel import User


class CompanyEmployee(User):
    employee_id: int
    company_id: int
    job_title: str

    class Config:
        orm_mode = True


class CompanyEmployeeCreate(BaseModel):
    user_id: int
    job_title: str
