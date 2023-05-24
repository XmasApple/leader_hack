import http.client

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import adminSchema, platformSchema
from crud import adminCrud, platformCrud

router = APIRouter(prefix="/admin")


@router.post("/add/", response_model=adminSchema.Admin)
def add_admin(admin: adminSchema.AdminCreate, db: Session = Depends(get_db)):
    if adminCrud.get_admin_by_user_id(db, user_id=admin.user_id) is None:
        return adminCrud.add_admin(db=db, admin=admin)
    else:
        raise HTTPException(status_code=400, detail="Admin already added")


@router.delete("/delete/{admin_id}", response_model=adminSchema.Admin)
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = adminCrud.get_admin(db=db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=400, detail="Admin does not exist")
    return adminCrud.remove_admin(db=db, admin_id=admin_id)


@router.put("/hide-platform/{platform_id}")
def hide_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform(db=db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=400, detail="Platform does not exist")
    platformCrud.hide_platform_by_admin(db=db, platform_id=platform_id)
    return http.client.OK
