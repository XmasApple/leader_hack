from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import schemas.all_schemas as schemas
from crud import platformCrud, userCrud
from database import get_db

router = APIRouter(prefix='/platforms', tags=['platforms'])


@router.post("/add/", response_model=schemas.Platform)
def add_platform(platform: schemas.PlatformCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_id(db, user_id=platform.owner_id)
    db_platform = platformCrud.get_platform_by_name(db, platform.name)

    if db_user is None:
        raise HTTPException(status_code=400, detail="The owner with that id does not exist")
    if db_platform:
        raise HTTPException(status_code=400, detail="The platform with that name is already registered")

    return platformCrud.create_platform(db=db, platform=platform)


@router.get("/{platform_id}", response_model=schemas.Platform)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform(db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@router.get("/name/{name}", response_model=schemas.Platform)
def read_platform_by_name(name: str, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform_by_name(db, platform_name=name)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@router.get("/", response_model=list[schemas.Platform])
def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = platformCrud.get_all_platforms(db, skip=skip, limit=limit)
    return platforms
