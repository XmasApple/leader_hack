from pydantic import BaseModel


class AdminBase(BaseModel):
    user_id: int


class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True


class AdminCreate(AdminBase):
    pass
