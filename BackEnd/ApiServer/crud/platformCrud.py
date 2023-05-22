from sqlalchemy.orm import Session
from models import platformModel
from schemas import platformSchema


def get_platform(db: Session, platform_id: int):
    return db.query(platformModel.Platform).filter(platformModel.Platform.platform_id == platform_id).first()


def get_platform_by_name(db: Session, platform_name: str):
    return db.query(platformModel.Platform).filter(platformModel.Platform.name.contains(platform_name)).first()


def get_all_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(platformModel.Platform).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: platformSchema.PlatformCreate):
    db_platform = platformModel.Platform()
    db_platform.name = platform.name,
    db_platform.owner_id = platform.owner_id
    db_platform.type = platform.type
    db_platform.square = platform.square
    db_platform.ceiling_height = platform.ceiling_height
    db_platform.closest_station = platform.closest_station
    db_platform.price_per_hour = platform.price_per_hour
    db_platform.info = platform.info

    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform
