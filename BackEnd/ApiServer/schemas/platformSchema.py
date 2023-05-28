from pydantic import BaseModel
import models.all_models as models


class PlatformBase(BaseModel):
    name: str
    platform_type_id: int
    square: float
    ceiling_height: float
    closest_station: str = None
    people_capacity: int
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
    hidden_by_user: int
    hidden_by_admin: int
    is_verified: int

    class Config:
        orm_mode = True


class PlatformFull(Platform):
    images: list[str] = []
    company_phone_number: str = None
    platform_feedbacks: list[tuple(int, float)] = []

    @staticmethod
    def from_db_platform_and_images(db_platform: models.Platform, db_images: list[models.PlatformImage],
                                    db_company: models.Company,
                                    db_platform_feedbacks: list[models.PlatformFeedback] = []):
        return PlatformFull(
            name=db_platform.name,
            platform_type_id=db_platform.platform_type_id,
            square=db_platform.square,
            ceiling_height=db_platform.ceiling_height,
            closest_station=db_platform.closest_station,
            people_capacity=db_platform.people_capacity,
            rent_type=db_platform.rent_type,
            price_per_time=db_platform.price_per_time,
            description=db_platform.description,
            geotag=db_platform.geotag,
            main_image=db_platform.main_image,
            platform_id=db_platform.platform_id,
            company_id=db_platform.company_id,
            company_phone_number=db_company.phone_number,
            images=[image.image for image in db_images],
            feedbacks=[(db_feedback.rating, db_feedback.feedback) for db_feedback in db_platform_feedbacks],
            hidden_by_user=db_platform.hidden_by_user,
            hidden_by_admin=db_platform.hidden_by_admin,
            is_verified=db_platform.is_verified
        )
