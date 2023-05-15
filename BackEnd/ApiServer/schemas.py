from pydantic import BaseModel
from datetime import datetime

# User and Owner
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

"""class Owner(User):
    telephone: str"""

# Platform
class PlatformBase(BaseModel):
    name: str
    type: str
    square: float
    ceiling_height: float
    closest_station: str
    price_per_hour: float
    info: str

class Platform(PlatformBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Booking
class BookingBase(BaseModel):
    number_of_persons: int
    start_date: datetime
    end_date: datetime

class Booking(BookingBase):
    id: int
    platform_id: int

    class Config:
        orm_mode = True

