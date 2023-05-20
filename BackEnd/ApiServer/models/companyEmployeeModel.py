from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from models.companyModel import Company
from models.userModel import User


class CompanyEmployee(Base):
    __tablename__ = "company_employees"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey(f"{Company.__tablename__}.id"))
    user_id = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
    job_title = Column(String, nullable=False)
