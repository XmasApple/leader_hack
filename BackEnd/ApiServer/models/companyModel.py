from sqlalchemy import Column, Integer, String

from database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    TIN = Column(String(12), unique=True, nullable=False)
    company_name = Column(String, unique=True, nullable=False)
    company_legal_name = Column(String, unique=True, nullable=False)
    company_phone_number = Column(String(11), unique=True, nullable=False)
    description = Column(String, nullable=False)
