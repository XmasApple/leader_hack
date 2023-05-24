from sqlalchemy.orm import Session
import models.all_models as models
import schemas.all_schemas as schemas


def get_platform(db: Session, platform_id: int):
    return db.query(models.Platform).filter(models.Platform.platform_id == platform_id).first()


def get_platform_by_name(db: Session, platform_name: str):
    return db.query(models.Platform).filter(models.Platform.name.contains(platform_name)).first()


def get_all_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: schemas.PlatformCreate):
    db_platform = models.Platform()
    db_platform.name = platform.name,
    db_platform.owner_id = platform.owner_id,
    db_platform.type = platform.type,
    db_platform.square = platform.square,
    db_platform.ceiling_height = platform.ceiling_height,
    db_platform.closest_station = platform.closest_station,
    db_platform.price_per_hour = platform.price_per_hour,
    db_platform.info = platform.info,
    db_platform.hidden_by_admin = platform.hidden_by_admin,
    db_platform.hidden_by_user = platform.hidden_by_user

    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform


# route = ~/platforms/hide-platform/{id}
def hide_platform_by_user(db: Session, platform_id: int):
    db_platform = get_platform(db=db, platform_id=platform_id)
    db_platform.hidden_by_user = 1
    db.commit()


# route = ~/admin/hide-platform/{id}
def hide_platform_by_admin(db: Session, platform_id: int):
    db_platform = get_platform(db=db, platform_id=platform_id)
    db_platform.hidden_by_admin = 1
    db.commit()
