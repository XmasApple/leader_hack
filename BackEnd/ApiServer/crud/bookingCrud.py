from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime
import models.all_models as models
import schemas.all_schemas as schemas


def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()


def get_booking_by_place(db: Session, platform_id: int):
    return db.query(models.Booking).filter(models.Booking.platform_id == platform_id)


def get_booking_by_time(db: Session, platform_id: int, start_time: datetime, end_time: datetime):
    return db.query(models.Booking).filter(
        and_(
            models.Booking.platform_id == platform_id,
            models.Booking.start_date.between(start_time, end_time),
            models.Booking.end_date.between(start_time, end_time)
        )).first()


def get_all_booking(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()


def add_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking()
    db_booking.platform_id = booking.platform_id
    db_booking.number_of_persons = booking.number_of_persons
    db_booking.start_date = booking.start_date
    db_booking.end_date = booking.end_date

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
