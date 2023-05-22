from sqlalchemy.orm import Session
import models.all_models as models
import schemas.all_schemas as schemas


def get_platform_by_id(db: Session, platform_id: int):
    return db.query(models.Platform).filter(models.Platform.platform_id == platform_id).first()


def get_platforms_by_name(db: Session, platform_name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).filter(models.Platform.name.contains(platform_name)).offset(skip).limit(
        limit).all()


def get_platform_by_name(db: Session, platform_name: str):
    return db.query(models.Platform).filter(models.Platform.name == platform_name).first()


def get_all_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: schemas.PlatformCreate, company_id: int):
    db_platform = models.Platform(
        name=platform.name,
        company_id=company_id,
        platform_type_id=platform.platform_type_id,
        square=platform.square,
        ceiling_height=platform.ceiling_height,
        closest_station=platform.closest_station,
        rent_type=platform.rent_type,
        price_per_time=platform.price_per_time,
        description=platform.description,
        geotag=platform.geotag,
        main_image=platform.main_image
    )
    # images = platform.images
    # for image in images:
    #
    print(db_platform.__dict__)

    images = [models.PlatformImage(image=image, platform_id=db_platform.platform_id) for image in platform.images]

    db.add(db_platform)
    db.commit()
    db.add_all(images)
    db.commit()
    db.refresh(db_platform)
    return db_platform, images


def get_platform_types(db: Session):
    return db.query(models.PlatformType).all()
