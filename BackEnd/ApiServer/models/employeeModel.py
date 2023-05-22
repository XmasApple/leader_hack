from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from models.companyModel import Company
from models.userModel import User


class Employee(Base):
    __tablename__ = "company_employees"

    employee_id: Column = Column(Integer, primary_key=True, index=True)
    company_id: Column = Column(Integer, ForeignKey(f"{Company.__tablename__}.company_id"))
    user_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
    job_title: Column = Column(String, nullable=False)
