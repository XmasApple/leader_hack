import hashlib

from sqlalchemy.orm import Session
import models
import schemas

# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    # use sha256 to hash password
    h = hashlib.sha256()
    h.update(user.password.encode('utf-8'))
    hashed_password = h.hexdigest()

    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_user_password(db: Session, user: schemas.UserCreate):
    db_user = get_user_by_email(db, user.email)

    if db_user:
        h = hashlib.sha256()
        h.update(user.password.encode('utf-8'))
        hashed_password = h.hexdigest()
        return db_user.hashed_password == hashed_password
    return False


def get_user_id_by_email(db: Session, email: str):
    db_user = get_user_by_email(db, email)
    if db_user:
        return db_user.id
    return None


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Platfomrs 
def get_platform(db: Session, platform_id: int):
    return db.query(models.Platform).filter(models.Platform.id == platform_id).first()

def get_platform_by_name(db: Session, platform_name: str):
    return db.query(models.Platform).filter(models.Platform.name == platform_name).first()

def create_platform(db: Session, platform: schemas.Platform):
    db_platform = models.Platform()
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

# Booking
def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id.first())
                                           
def add_booking(db: Session, booking: schemas.Booking):
    db_booking = models.Booking()
    db_booking.platform_id = booking.platform_id
    db_booking.number_of_persons = booking.number_of_persons
    db_booking.start_date = booking.start_date
    db_booking.end_date = booking.end_date

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking