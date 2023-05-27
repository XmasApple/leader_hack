from datetime import datetime

from sqlalchemy import and_, or_, Float
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import cast

import models.all_models as models
import schemas.all_schemas as schemas


# def get_booking(db: Session, booking_id: int):
#     return db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()
#
#
# def get_booking_by_place(db: Session, platform_id: int):
#     return db.query(models.Booking).filter(models.Booking.platform_id == platform_id)
#
#
# def get_booking_by_time(db: Session, platform_id: int, start_time: datetime, end_time: datetime):
#     return db.query(models.Booking).filter(
#         and_(
#             models.Booking.platform_id == platform_id,
#             models.Booking.start_date.between(start_time, end_time),
#             models.Booking.end_date.between(start_time, end_time)
#         )).first()
#
#
# def get_all_booking(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Booking).offset(skip).limit(limit).all()
#
#
# def add_booking(db: Session, booking: schemas.BookingCreate):
#     db_booking = models.Booking()
#     db_booking.platform_id = booking.platform_id
#     db_booking.number_of_persons = booking.number_of_persons
#     db_booking.start_date = booking.start_date
#     db_booking.end_date = booking.end_date
#
#     db.add(db_booking)
#     db.commit()
#     db.refresh(db_booking)
#     return db_booking


def get_user_bookings_by_token(db: Session, token: str):
    records = db.query(models.Token, models.Booking).filter(
        and_(
            models.Token.user_id == models.Booking.user_id,
            models.Token.token == token
        )
    ).all()

    db_bookings = [record[1] for record in records]

    return db_bookings


def get_booking_collisions(db: Session, booking: schemas.BookingCreate):
    records = db.query(models.Booking).filter(
        and_(
            models.Booking.platform_id == booking.platform_id,
            or_(
                models.Booking.start_date.between(booking.start_date, booking.end_date),
                models.Booking.end_date.between(booking.start_date, booking.end_date)
            )
        )
    ).first()

    return records


def create_booking(db: Session, booking: schemas.BookingCreate, token: str):
    query_result = db.query(models.Token, models.User).filter(
        and_(
            models.Token.user_id == models.User.user_id,
            models.Token.token == token
        )
    ).first()

    if query_result is None:
        return "Invalid token"
    db_user = query_result[1]

    db_platform = db.query(models.Platform).filter(
        models.Platform.platform_id == booking.platform_id
    ).first()

    if db_platform is None:
        return "Invalid platform id"

    db_collisions = get_booking_collisions(db, booking)
    if db_collisions is not None:
        return "Booking collision"

    if booking.start_date < datetime.now() or booking.end_date < datetime.now():
        return "Invalid start and end date"

    if booking.number_of_persons > db_platform.people_capacity:
        return "Invalid number of persons"

    # price_per_time = db_platform.price_per_time
    price_per_time = cast(db_platform.price_per_time, Float)
    if booking.rent_type == 1:
        hours = (booking.end_date - booking.start_date).total_seconds() / 3600
        if hours < 1:
            return "Invalid start and end date"
        price = price_per_time * hours
    elif booking.rent_type == 2:
        days = (booking.end_date - booking.start_date).days
        if days < 1:
            return "Invalid start and end date"
        price = price_per_time * days
    else:
        return "Invalid rent type"

    db_booking = models.Booking(
        user_id=db_user.user_id,
        platform_id=booking.platform_id,
        number_of_persons=booking.number_of_persons,
        start_date=booking.start_date,
        end_date=booking.end_date,
        rent_type=booking.rent_type,
        comment=booking.comment,
        price=price
    )

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_user_booking_by_id(db: Session, booking_id: int, token: str):
    query_result = db.query(models.Token, models.Booking).filter(
        and_(
            models.Token.user_id == models.Booking.user_id,
            models.Token.token == token,
            models.Booking.booking_id == booking_id
        )
    ).first()
    return query_result[1]


def get_user_platform_booking(db: Session, platform_id: int, token: str):
    query_result = db.query(models.Token, models.Booking).filter(
        and_(
            models.Token.user_id == models.Booking.user_id,
            models.Token.token == token,
            models.Booking.platform_id == platform_id
        )).first()

    if query_result is None:
        return None

    db_booking = query_result[1]
    return db_booking


def get_company_booking_by_id(db: Session, booking_id: int, token: str):
    query_result = db.query(
        models.Token, models.Employee, models.Company).filter(
        and_(
            models.Token.user_id == models.Employee.user_id,
            models.Employee.company_id == models.Company.company_id,
            models.Token.token == token,
            models.Booking.booking_id == booking_id
        )).first()

    if query_result is None:
        return None

    db_booking = query_result[1]
    return db_booking


def get_company_platform_bookings(db: Session, platform_id: int, token: str):
    query_result = db.query(
        models.Token, models.Employee, models.Company, models.Platform).filter(
        and_(
            models.Token.user_id == models.Employee.user_id,
            models.Employee.company_id == models.Company.company_id,
            models.Company.company_id == models.Platform.company_id,
            models.Token.token == token,
            models.Platform.platform_id == platform_id
        )).all()

    if query_result is None:
        return None

    db_platforms = [record[3] for record in query_result]
    return db_platforms
