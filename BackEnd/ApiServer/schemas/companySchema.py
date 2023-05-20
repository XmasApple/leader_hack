from pydantic import BaseModel


class Company(BaseModel):
    id: int
    tin: str
    name: str
    legal_name: str
    phone_number: str
    description: str


class CompanyCreate(Company):
    job_title: str
