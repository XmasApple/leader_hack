from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USers
@app.post("/users/create/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/auth/", response_model=schemas.User)
def auth_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.check_user_password(db, user):
        user_id = crud.get_user_id_by_email(db, user.email)
        return crud.get_user(db, user_id)
    raise HTTPException(status_code=400, detail="Incorrect email or password")

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users

# Platforms
@app.post("/platforms/add/", response_model=schemas.Platform)
def add_platform(platform: schemas.Platform, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=platform.owner_id)
    db_platform = crud.get_platform_by_name(db, platform.name)

    if db_user is None:
        raise HTTPException(status_code=400, detail="The owner with that id does not exist")
    if db_platform:
        raise HTTPException(status_code=400, detail="The platform with that name is already registered")
    
    return crud.create_platform(db=db, platform=platform)

@app.get("/platforms/{id}", response_model=schemas.Platform)
def read_platform(id: int, db: Session = Depends(get_db)):
    db_platform = crud.get_platform(db, platform_id=id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform

@app.get("/platforms/name/{name}", response_model=schemas.Platform)
def read_platform_by_name(name: str, db: Session = Depends(get_db)):
    db_platform = crud.get_platform_by_name(db, platform_name=name)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform

@app.get("/platforms/", response_model=list[schemas.Platform])
def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = crud.get_all_platforms(db, skip=skip, limit=limit)
    return platforms

# Booking
@app.post("/booking/add/", response_model=schemas.Booking)
def add_booking(booking: schemas.Booking, db: Session = Depends(get_db)):
    db_platform = crud.get_platform(db, platform_id=booking.platform_id)
    db_booking = crud.get_booking_by_time(db, platform_id=booking.platform_id,
                                            start_time=booking.start_date, end_time=booking.end_date)
    
    if db_platform is None:
        raise HTTPException(status_code=400, detail="The platform with that id does not exist")
    if db_booking:
        raise HTTPException(status_code=400, detail="Booking with that time and place is already registered")

    return crud.add_booking(db, booking=booking)

@app.get("/booking/{id}", response_model=schemas.Booking)
def read_booking(id: int, db: Session = Depends(get_db)):
    db_booking = crud.get_booking(db, booking_id=id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@app.get("/booking/", response_model=list[schemas.Booking])
def read_all_booking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booking = crud.get_all_booking(db, skip=skip, limit=limit)
    return booking