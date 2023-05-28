from sqlalchemy import and_
from sqlalchemy.orm import Session

import models.all_models as models
import schemas.all_schemas as schemas


def get_platform_by_id(db: Session, platform_id: int,
                       hidden_by_admin: bool = False,
                       hidden_by_user: bool = False,
                       is_verified: bool = True):
    return db.query(models.Platform).filter(
        and_(models.Platform.platform_id == platform_id,
             models.Platform.hidden_by_admin == int(hidden_by_admin),
             models.Platform.hidden_by_user == int(hidden_by_user),
             models.Platform.is_verified == int(is_verified)
             )).first()


def get_full_platform_by_id(db: Session, platform_id: int):
    db_platform = db.query(models.Platform).filter(
        and_(models.Platform.platform_id == platform_id,
             models.Platform.hidden_by_admin == 0,
             models.Platform.hidden_by_user == 0,
             models.Platform.is_verified == 1
             )).first()
    if db_platform is None:
        return None, None
    db_images = db.query(models.PlatformImage).filter(models.PlatformImage.platform_id == platform_id).all()
    db_company = db.query(models.Company).filter(models.Company.company_id == db_platform.company_id).first()
    return db_platform, db_images, db_company


def get_platforms_by_name(db: Session, platform_name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).filter(
        and_(models.Platform.name.contains(platform_name),
             models.Platform.hidden_by_admin == 0,
             models.Platform.hidden_by_user == 0,
             models.Platform.is_verified == 1
             )).offset(skip).limit(limit).all()


def get_all_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).filter(
        and_(models.Platform.hidden_by_admin == 0,
             models.Platform.hidden_by_user == 0,
             models.Platform.is_verified == 1)
    ).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: schemas.PlatformCreate, company_id: int):
    db_platform = models.Platform(
        name=platform.name,
        company_id=company_id,
        platform_type_id=platform.platform_type_id,
        square=platform.square,
        ceiling_height=platform.ceiling_height,
        closest_station=platform.closest_station,
        people_capacity=platform.people_capacity,
        rent_type=platform.rent_type,
        price_per_time=platform.price_per_time,
        description=platform.description,
        geotag=platform.geotag,
        main_image=platform.main_image
    )

    db.add(db_platform)
    db.commit()

    platform_id = db.query(models.Platform).filter(models.Platform.name == platform.name).first().platform_id

    images = [models.PlatformImage(image=image, platform_id=platform_id) for image in platform.images]

    db.add_all(images)
    db.commit()
    db.refresh(db_platform)
    return db_platform, images


def get_platform_types(db: Session):
    return db.query(models.PlatformType).all()


# route = ~/platforms/hide-platform/{id}
def platform_set_hide_by_user(db: Session, platform_id: int, hide: bool):
    db_platform = get_platform_by_id(db=db, platform_id=platform_id)
    if db_platform is None:
        return None
    db_platform.hidden_by_user = int(hide)
    db.commit()
    db.refresh(db_platform)
    return db_platform


def add_feedback(db: Session, platform_feedback: schemas.PlatformFeedback):
    db_feedback = models.PlatformFeedback(
        platform_feedback_id = platform_feedback.platform_feedback_id,
        platform_id = platform_feedback.platform_id,
        rating = platform_feedback.rating,
        feedback = platform_feedback.feedback
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


def get_feedbacks(db: Session, platform_id: int):
    return db.query(models.PlatformFeedback).filter(models.PlatformFeedback.platform_id == platform_id).all()
