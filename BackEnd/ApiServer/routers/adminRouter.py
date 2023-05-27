from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

import schemas.all_schemas as schemas
from crud import adminCrud, userCrud
from database import get_db

router = APIRouter(prefix="/admin", tags=['admin'])

auth_scheme = HTTPBearer()


@router.post("/add/", response_model=schemas.Admin)
def add_admin(new_admin: schemas.AdminCreate,
              db: Session = Depends(get_db),
              token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    db_user = userCrud.get_user_by_id(db, user_id=new_admin.user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User does not exist")
    if adminCrud.get_admin_by_user_id(db, user_id=new_admin.user_id) is not None:
        raise HTTPException(status_code=400, detail="Admin already added")

    return adminCrud.add_admin(db=db, admin=new_admin)


@router.delete("/delete/{admin_id}", response_model=schemas.Admin)
def delete_admin(admin_id: int,
                 db: Session = Depends(get_db),
                 token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    return adminCrud.remove_admin(db=db, admin_id=admin_id)


def set_platform_hide(db: Session, platform_id: int, hide: bool, token: HTTPAuthorizationCredentials):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    db_platform = adminCrud.set_platform_hide(db=db, platform_id=platform_id, hide=hide)
    if db_platform is None:
        raise HTTPException(status_code=400, detail="Platform does not exist")
    return db_platform


@router.post("/hide_platform/{platform_id}", response_model=schemas.Platform)
def hide_platform(platform_id: int,
                  db: Session = Depends(get_db),
                  token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return set_platform_hide(db, platform_id, True, token)


@router.post("/unhide_platform/{platform_id}", response_model=schemas.Platform)
def unhide_platform(platform_id: int,
                    db: Session = Depends(get_db),
                    token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return set_platform_hide(db, platform_id, False, token)


@router.post("/verify_platform/{platform_id}", response_model=schemas.Platform)
def verify_platform(platform_id: int,
                    db: Session = Depends(get_db),
                    token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    db_platform = adminCrud.verify_platform(db=db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=400, detail="Platform does not exist")

    return db_platform


@router.post("/verify_company/{company_id}", response_model=schemas.Company)
def verify_company(company_id: int,
                   db: Session = Depends(get_db),
                   token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    db_company = adminCrud.verify_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=400, detail="Company does not exist")

    return db_company


@router.get("/get_unverified_platforms/", response_model=list[schemas.Platform])
def get_unverified_platforms(db: Session = Depends(get_db),
                             token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials

    db_admin = adminCrud.get_admin_by_token(db, token)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Incorrect token")
    return adminCrud.get_unverified_platforms(db=db)
