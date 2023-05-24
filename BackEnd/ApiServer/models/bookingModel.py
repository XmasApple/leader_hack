from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, CheckConstraint, String
from database import Base
from models.platformModel import Platform
from models.userModel import User


class Booking(Base):
    __tablename__ = "booking"
    __table_args__ = (
        CheckConstraint("rent_type in (1, 2)"),
    )

    booking_id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"), nullable=False)
    platform_id: Column = Column(Integer, ForeignKey(f"{Platform.__tablename__}.platform_id"))
    number_of_persons: Column = Column(Integer)
    start_date: Column = Column(DateTime, nullable=False)
    end_date: Column = Column(DateTime, nullable=False)
    rent_type: Column = Column(Integer, nullable=False)
    price: Column = Column(Integer, nullable=False)
    status: Column = Column(Integer, nullable=False, default=1)
    comment: Column = Column(String)
    created_at: Column = Column(DateTime, nullable=False, default=datetime.now())
