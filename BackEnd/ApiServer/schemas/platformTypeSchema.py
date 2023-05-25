from pydantic import BaseModel


class PlatformType(BaseModel):
    platform_type_id: int
    name: str

    class Config:
        orm_mode = True
