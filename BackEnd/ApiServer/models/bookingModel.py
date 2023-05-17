from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    number_of_persons = Column(Integer)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)