from pydantic import BaseModel


# class PlatformBase(BaseModel):
#     name: str
#     type: str
#     square: float
#     ceiling_height: float
#     closest_station: str
#     price_per_hour: float
#     info: str
#     owner_id: int
#
#
# class Platform(PlatformBase):
#     platform_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class PlatformCreate(PlatformBase):
#     pass

class PlatformBase(BaseModel):
    name: str
    platform_type_id: int
    square: float
    ceiling_height: float
    closest_station: str = None
    rent_type: int
    price_per_time: float
    description: str = None
    geotag: str = None
    main_image: str = None


class PlatformCreate(PlatformBase):
    images: list[str] = []


class Platform(PlatformBase):
    platform_id: int
    company_id: int

    class Config:
        orm_mode = True


class PlatformFull(Platform):
    images: list[str] = []
