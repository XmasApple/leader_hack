from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime
from models import bookingModel
from schemas import bookingSchema


def get_booking(db: Session, booking_id: int):
    return db.query(bookingModel.Booking).filter(bookingModel.Booking.booking_id == booking_id).first()


def get_booking_by_place(db: Session, platform_id: int):
    return db.query(bookingModel.Booking).filter(bookingModel.Booking.platform_id == platform_id)


def get_booking_by_time(db: Session, platform_id: int, start_time: datetime, end_time: datetime):
    return db.query(bookingModel.Booking).filter(
        and_(
            bookingModel.Booking.platform_id == platform_id,
            bookingModel.Booking.start_date.between(start_time, end_time),
            bookingModel.Booking.end_date.between(start_time, end_time)
        )).first()


def get_all_booking(db: Session, skip: int = 0, limit: int = 100):
    return db.query(bookingModel.Booking).offset(skip).limit(limit).all()


def add_booking(db: Session, booking: bookingSchema.BookingCreate):
    db_booking = bookingModel.Booking()
    db_booking.platform_id = booking.platform_id
    db_booking.number_of_persons = booking.number_of_persons
    db_booking.start_date = booking.start_date
    db_booking.end_date = booking.end_date

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
