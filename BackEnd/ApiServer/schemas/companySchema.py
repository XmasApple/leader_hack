from pydantic import BaseModel


class CompanyBase(BaseModel):
    TIN: str
    name: str
    legal_name: str
    phone_number: str = '79991112233'
    description: str


class CompanyCreate(CompanyBase):
    job_title: str


class Company(CompanyBase):
    company_id: int
    owner_id: int

    class Config:
        orm_mode = True
