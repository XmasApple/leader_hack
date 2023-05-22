from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base
from models.platformModel import Platform


class Booking(Base):
    __tablename__ = "booking"

    booking_id: Column = Column(Integer, primary_key=True, index=True)
    platform_id: Column = Column(Integer, ForeignKey(f"{Platform.__tablename__}.platform_id"))
    number_of_persons: Column = Column(Integer)
    start_date: Column = Column(DateTime, nullable=False)
    end_date: Column = Column(DateTime, nullable=False)
