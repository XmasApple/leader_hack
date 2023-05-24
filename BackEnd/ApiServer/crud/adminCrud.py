from sqlalchemy.orm import Session
from models import adminModel
from schemas import adminSchema


def add_admin(db: Session, admin: adminSchema.AdminCreate):
    db_admin = adminModel.Admin(user_id=admin.user_id)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def get_admin(db: Session, admin_id: int):
    return db.query(adminModel.Admin).filter(adminModel.Admin.id == admin_id).first()


def get_admin_by_user_id(db: Session, user_id: int):
    return db.query(adminModel.Admin).filter(adminModel.Admin.user_id == user_id).first()


def remove_admin(db: Session, admin_id: int):
    db_admin = get_admin(db=db, admin_id=admin_id)

    db.delete(db_admin)
    db.commit()
    return db_admin
