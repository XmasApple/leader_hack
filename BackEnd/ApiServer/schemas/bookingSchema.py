from pydantic import BaseModel
from datetime import datetime


class BookingBase(BaseModel):
    user_id: int
    platform_id: int
    number_of_persons: int
    start_date: datetime
    end_date: datetime
    rent_type: int
    comment: str = None


class Booking(BookingBase):
    booking_id: int
    status: int
    price: int = 0

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass
