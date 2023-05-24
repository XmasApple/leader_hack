import http

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import platformSchema
from crud import platformCrud, userCrud

router = APIRouter(prefix='/platforms')


@router.post("/add/", response_model=platformSchema.Platform)
def add_platform(platform: platformSchema.PlatformCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=platform.owner_id)
    db_platform = platformCrud.get_platform_by_name(db, platform.name)

    if db_user is None:
        raise HTTPException(status_code=400, detail="The owner with that id does not exist")
    if db_platform:
        raise HTTPException(status_code=400, detail="The platform with that name is already registered")

    return platformCrud.create_platform(db=db, platform=platform)


@router.get("/{platform_id}", response_model=platformSchema.Platform)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform(db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@router.get("/name/{name}", response_model=platformSchema.Platform)
def read_platform_by_name(name: str, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform_by_name(db, platform_name=name)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@router.get("/", response_model=list[platformSchema.Platform])
def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = platformCrud.get_all_platforms(db, skip=skip, limit=limit)
    return platforms


@router.put("/hide-platform/{platform_id}")
def hide_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform(db=db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=400, detail="Platform does not exist")
    platformCrud.hide_platform_by_user(db=db, platform_id=platform_id)
    return http.client.OK
