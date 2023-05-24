from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base

from models.platformModel import Platform


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    platform_id = Column(Integer, ForeignKey(f"{Platform.__tablename__}.id"))
    number_of_persons = Column(Integer)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
