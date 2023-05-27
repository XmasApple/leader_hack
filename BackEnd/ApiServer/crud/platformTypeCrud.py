from sqlalchemy.orm import Session

from database import  engine
from models import platformTypeModel
from schemas import platformTypeSchema
from enums import PlatformTypeEnum


def add_platform_type(db: Session, platform_type: platformTypeSchema.PlatformType):
    db_platform_type = platformTypeModel.PlatformType()
    db_platform_type.name = platform_type.name
    db_platform_type.id = platform_type.id

    db.add(db_platform_type)
    db.commit()
    db.refresh(db_platform_type)
    return db_platform_type


def get_platform_type_by_name(db: Session, platform_name: str):
    return db.query(platformTypeModel.PlatformType).filter(platformTypeModel.PlatformType.name == platform_name).first()


def get_platform_type(db: Session, platform_id: int):
    return db.query(platformTypeModel.PlatformType).filter(platformTypeModel.PlatformType.id == platform_id).first()


def del_platform_type(db: Session, platform_name: str):
    db_platform_type = get_platform_type_by_name(db=db, platform_name=platform_name)
    db.delete(db_platform_type)
    db.commit()
    return db_platform_type


def init_platform_types():
    with Session(autoflush=False, bind=engine) as db:
        for platform_type in PlatformTypeEnum:
            if get_platform_type(db=db, platform_id=platform_type.value) is not None:
                continue
            db_platform_type = platformTypeModel.PlatformType()
            db_platform_type.id = platform_type.value
            db_platform_type.name = platform_type.name

            db.add(db_platform_type)
            db.commit()
