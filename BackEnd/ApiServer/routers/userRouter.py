from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from crud import userCrud, adminCrud
from database import get_db
import schemas.all_schemas as schemas

router = APIRouter(prefix='/users', tags=['users'])

auth_scheme = HTTPBearer()


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_all_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/create/", response_model=schemas.Token)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # return userCrud.create_user(db=db, user=user)
    db_user = userCrud.create_user(db=db, user=user)
    db_token = userCrud.create_token(db=db, user_id=db_user.user_id, life_time=user.life_time)
    return db_token


@router.post("/auth/", response_model=schemas.Token)
def auth_user(user: schemas.UserAuth, db: Session = Depends(get_db), ):
    if not userCrud.check_user_password(db, user):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    user_id = userCrud.get_user_id_by_email(db, user.email)
    if user_id is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    db_token = userCrud.create_token(db=db, user_id=user_id, life_time=user.life_time)
    return db_token


@router.get("/me/", response_model=Union[schemas.User, schemas.Employee, schemas.Admin])
def read_user_me(token: HTTPAuthorizationCredentials = Depends(auth_scheme),
                 db: Session = Depends(get_db)):
    token = token.credentials
    if not userCrud.check_token(db, token):
        raise HTTPException(status_code=400, detail="Incorrect token")
    user = userCrud.get_user_by_token(db, token)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    admin = adminCrud.get_admin_by_user(db, user)
    if admin:
        return admin
    employee = userCrud.get_employee(db, user)
    if employee:
        return employee
    return user


@router.post("/change-password/", response_model=schemas.Token)
def change_password(user: schemas.UserAuth,
                    db: Session = Depends(get_db),
                    token: HTTPAuthorizationCredentials = Depends(auth_scheme)):

    token = token.credentials
    db_user = userCrud.get_user_by_token(db=db, token=token)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found or incorrect token")

    return userCrud.change_user_password(db=db, user=db_user, new_password=user.password)
