from pydantic import BaseModel


class PlatformTypeBase(BaseModel):
    name: str


class PlatformType(PlatformTypeBase):
    id: int

    class Config:
        orm_mode = True


class PlatformTypeCreate(PlatformTypeBase):
    pass
