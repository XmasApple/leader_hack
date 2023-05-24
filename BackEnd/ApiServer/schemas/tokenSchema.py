from pydantic import BaseModel


class Token(BaseModel):
    token: str
    expire_date: str

    class Config:
        orm_mode = True
