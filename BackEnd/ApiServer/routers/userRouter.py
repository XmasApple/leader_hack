from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import userSchema
from crud import userCrud

router = APIRouter(prefix='/users')


@router.post("/create/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userCrud.create_user(db=db, user=user)


@router.post("/auth/", response_model=userSchema.User)
def auth_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    if userCrud.check_user_password(db, user):
        user_id = userCrud.get_user_id_by_email(db, user.email)
        return userCrud.get_user(db, user_id)
    raise HTTPException(status_code=400, detail="Incorrect email or password")


@router.get("/{user_id}", response_model=userSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[userSchema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_all_users(db, skip=skip, limit=limit)
    return users
