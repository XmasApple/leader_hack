from pydantic import BaseModel
from datetime import datetime


class BookingBase(BaseModel):
    number_of_persons: int
    start_date: datetime
    end_date: datetime
    platform_id: int


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass
