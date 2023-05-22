from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    user_id: int
    job_title: str


class Employee(EmployeeCreate):
    employee_id: int
    company_id: int
    job_title: str

    class Config:
        orm_mode = True
