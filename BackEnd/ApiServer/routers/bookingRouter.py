from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import bookingSchema
from crud import bookingCrud, platformCrud

router = APIRouter(prefix='/booking', tags=['booking'])


@router.post("/add/", response_model=bookingSchema.Booking)
def add_booking(booking: bookingSchema.BookingCreate, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform_by_id(db, platform_id=booking.platform_id)
    db_booking = bookingCrud.get_booking_by_time(db, platform_id=booking.platform_id,
                                                 start_time=booking.start_date, end_time=booking.end_date)

    if db_platform is None:
        raise HTTPException(status_code=400, detail="The platform with that id does not exist")
    if db_booking:
        raise HTTPException(status_code=400, detail="Booking with that time and place is already registered")

    return bookingCrud.add_booking(db, booking=booking)


@router.get("/{booking_id}", response_model=bookingSchema.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = bookingCrud.get_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@router.get("/", response_model=list[bookingSchema.Booking])
def read_all_booking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booking = bookingCrud.get_all_booking(db, skip=skip, limit=limit)
    return booking
