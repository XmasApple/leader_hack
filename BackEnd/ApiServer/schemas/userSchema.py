from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserAuth(UserBase):
    password: str
    life_time: int


class UserCreate(UserAuth):
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str


class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

