from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserAuth(UserBase):
    password: str
    life_time: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


"""class Owner(User):
    telephone: str"""