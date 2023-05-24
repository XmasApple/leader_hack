from pydantic import BaseModel


class PlatformBase(BaseModel):
    name: str
    type: str
    square: float
    ceiling_height: float
    closest_station: str
    price_per_hour: float
    info: str
    owner_id: int
    hidden_by_user: int


class Platform(PlatformBase):
    id: int

    class Config:
        orm_mode = True


class PlatformCreate(PlatformBase):
    hidden_by_admin: int = 0
