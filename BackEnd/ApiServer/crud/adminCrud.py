import hashlib
import http.client

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
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admin_by_user_id(db: Session, user_id: int):
    return db.query(models.Admin).filter(models.Admin.user_id == user_id).first()


def get_admin_by_user(db: Session, user: models.User):
    return db.query(models.Admin).filter(models.Admin.user_id == user.user_id).first()


def remove_admin(db: Session, admin_id: int):
    db_admin = get_admin(db=db, admin_id=admin_id)

    db.delete(db_admin)
    db.commit()
    return db_admin


def hide_platform(db: Session, platform_id: int):
    db_platform = platformCrud.get_platform(db=db, platform_id=platform_id)
    db_platform.hidden_by_admin = 1
    db.commit()


def delete_platform(db: Session, platform_id: int):
    db_platform = platformCrud.get_platform(db=db, platform_id=platform_id)

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


def change_user_password(db: Session, user: models.User):
    remove_tokens(db=db, user_id=user.user_id)
    h = hashlib.sha256()
    h.update(user.password.encode('utf-8'))
    hashed_password = h.hexdigest()
    user.hashed_password = hashed_password
    db.commit()

    return http.client.OK


def remove_tokens(db: Session, user_id: int):
    tokens: list = db.query(models.Token).filter(models.Token.user_id == user_id).all()
    for token in tokens:
        db.delete(token)
        db.commit()

    return http.client.OK

