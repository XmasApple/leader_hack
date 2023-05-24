from sqlalchemy import Column, Integer, String

from database import Base


class Company(Base):
    __tablename__ = "company"

    company_id: Column = Column(Integer, primary_key=True, index=True)
    owner_id: Column = Column(Integer, nullable=False)
    TIN: Column = Column(String(12), unique=True, nullable=False)
    name: Column = Column(String, unique=True, nullable=False)
    legal_name: Column = Column(String, unique=True, nullable=False)
    phone_number: Column = Column(String(11), unique=True, nullable=False)
    description: Column = Column(String, nullable=False)
