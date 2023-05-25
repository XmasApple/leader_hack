from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database import get_db
from schemas import bookingSchema
from crud import bookingCrud, platformCrud

router = APIRouter(prefix='/booking', tags=['booking'])

auth_scheme = HTTPBearer()


@router.get("/", response_model=list[bookingSchema.Booking])
def read_user_bookings(db: Session = Depends(get_db),
                       token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_bookings = bookingCrud.get_user_bookings_by_token(db, token)
    if db_bookings is None:
        raise HTTPException(status_code=404, detail="Bookings not found")
    return db_bookings


@router.get("/{booking_id}", response_model=bookingSchema.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db),
                 token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_booking = bookingCrud.get_user_booking_by_id(db, booking_id, token)

    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@router.post("/create/", response_model=bookingSchema.Booking)
def create_booking(booking: bookingSchema.BookingCreate,
                   db: Session = Depends(get_db),
                   token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    db_platform = platformCrud.get_platform_by_id(db, booking.platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")

    db_booking = bookingCrud.create_booking(db=db, booking=booking, token=token)
    if type(db_booking) == str:
        raise HTTPException(status_code=400, detail=db_booking)
    return db_booking

