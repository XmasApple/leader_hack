from sqlalchemy import Column, Integer, String, CheckConstraint, ForeignKey

from database import Base
from models.userModel import User


class Company(Base):
    __tablename__ = "company"
    __table_args__ = (
        CheckConstraint("is_verified in (0, 1)"),
    )

    company_id: Column = Column(Integer, primary_key=True, index=True)
    owner_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"), nullable=False, index=True,
                              unique=True)
    TIN: Column = Column(String(12), unique=True, nullable=False)
    name: Column = Column(String, unique=True, nullable=False)
    legal_name: Column = Column(String, unique=True, nullable=False)
    phone_number: Column = Column(String(11), unique=True, nullable=False)
    description: Column = Column(String, nullable=False)
    is_verified: Column = Column(Integer, nullable=False, default=0)
    logo = Column(String, nullable=False)
