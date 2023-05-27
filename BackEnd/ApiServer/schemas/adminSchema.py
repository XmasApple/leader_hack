from pydantic import BaseModel


class AdminBase(BaseModel):
    user_id: int


class Admin(AdminBase):
    admin_id: int

    class Config:
        orm_mode = True


class AdminCreate(AdminBase):
    pass
