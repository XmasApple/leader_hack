import http.client

from sqlalchemy import and_
from sqlalchemy.orm import Session

import models.all_models as models
import schemas.all_schemas as schemas
from crud import platformCrud, companyCrud, userCrud


def add_admin(db: Session, admin: schemas.AdminCreate):
    db_admin = models.Admin(user_id=admin.user_id)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def get_admin(db: Session, admin_id: int):
    return db.query(models.Admin).filter(models.Admin.admin_id == admin_id).first()


def get_admin_by_token(db: Session, token: str):
    db_query = db.query(models.Admin, models.Token).filter(
        and_(
            models.Admin.user_id == models.Token.user_id,
            models.Token.token == token
        )).first()
    if db_query is None:
        return None
    db_admin, db_token = db_query
    return db_admin


def get_admin_by_user_id(db: Session, user_id: int):
    return db.query(models.Admin).filter(models.Admin.user_id == user_id).first()


def get_admin_by_user(db: Session, user: models.User):
    return db.query(models.Admin).filter(models.Admin.user_id == user.user_id).first()


def remove_admin(db: Session, admin_id: int):
    db_admin = get_admin(db=db, admin_id=admin_id)

    db.delete(db_admin)
    db.commit()
    return db_admin


def set_platform_hide(db: Session, platform_id: int, hide: bool):
    db_platform = platformCrud.get_platform_by_id(db=db, platform_id=platform_id)
    if db_platform is None:
        return None
    db_platform.hidden_by_admin = int(hide)
    db.commit()
    db_platform = platformCrud.get_platform_by_id(db=db, platform_id=platform_id)
    return db_platform


def delete_platform(db: Session, platform_id: int):
    db_platform = platformCrud.get_platform_by_id(db=db, platform_id=platform_id)

    db.delete(db_platform)
    db.commit()
    return db_platform


def delete_company(db: Session, company_id: int):
    db_company = companyCrud.get_company(db=db, company_id=company_id)

    db.delete(db_company)
    db.commit()
    return db_company


def delete_user(db: Session, user_id: int):
    db_user = userCrud.get_user_by_id(db=db, user_id=user_id)

    db.delete(db_user)
    db.commit()
    return db_user


def remove_tokens(db: Session, user_id: int):
    tokens: list = db.query(models.Token).filter(models.Token.user_id == user_id).all()
    for token in tokens:
        db.delete(token)
        db.commit()

    return http.client.OK
