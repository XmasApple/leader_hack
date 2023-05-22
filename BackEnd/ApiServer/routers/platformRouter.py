from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

import schemas.all_schemas as schemas
from crud import platformCrud, userCrud, companyCrud
from database import get_db

router = APIRouter(prefix='/platforms', tags=['platforms'])

# @router.post("/add/", response_model=schemas.Platform)
# def add_platform(platform: schemas.PlatformCreate, db: Session = Depends(get_db)):
#     db_user = userCrud.get_user_by_id(db, user_id=platform.owner_id)
#     db_platform = platformCrud.get_platform_by_name(db, platform.name)
#
#     if db_user is None:
#         raise HTTPException(status_code=400, detail="The owner with that id does not exist")
#     if db_platform:
#         raise HTTPException(status_code=400, detail="The platform with that name is already registered")
#
#     return platformCrud.create_platform(db=db, platform=platform)
#
#
# @router.get("/{platform_id}", response_model=schemas.Platform)
# def read_platform(platform_id: int, db: Session = Depends(get_db)):
#     db_platform = platformCrud.get_platform(db, platform_id=platform_id)
#     if db_platform is None:
#         raise HTTPException(status_code=404, detail="Platform not found")
#     return db_platform
#
#
# @router.get("/name/{name}", response_model=schemas.Platform)
# def read_platform_by_name(name: str, db: Session = Depends(get_db)):
#     db_platform = platformCrud.get_platform_by_name(db, platform_name=name)
#     if db_platform is None:
#         raise HTTPException(status_code=404, detail="Platform not found")
#     return db_platform
#
#
# @router.get("/", response_model=list[schemas.Platform])
# def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     platforms = platformCrud.get_all_platforms(db, skip=skip, limit=limit)
#     return platforms

auth_scheme = HTTPBearer()


@router.get("/", response_model=list[schemas.Platform])
def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = platformCrud.get_all_platforms(db, skip=skip, limit=limit)
    print([platform.__dict__ for platform in platforms])
    return platforms


@router.get("/{platform_id}", response_model=schemas.Platform)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = platformCrud.get_platform_by_id(db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@router.get("/types/", response_model=list[schemas.PlatformType])
def read_platform_types(db: Session = Depends(get_db)):
    # return platformCrud.get_platform_types(db)
    platforms = platformCrud.get_platform_types(db)
    print([platform.__dict__ for platform in platforms])
    return platforms


@router.post("/create/", response_model=schemas.Platform)
def create_platform(platform: schemas.PlatformCreate,
                    db: Session = Depends(get_db),
                    token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = token.credentials
    # db_company = companyCrud.get_company_by_token(db, token)
    db_token, db_employee, db_company = companyCrud.get_company_by_token(db, token)
    if db_company is None:
        raise HTTPException(status_code=400, detail="Incorrect token or company does not exist")
    db_platform, db_images = platformCrud.create_platform(db=db, platform=platform, company_id=db_company.company_id)

    platform = schemas.Platform(
        name=db_platform.name,
        platform_type_id=db_platform.platform_type_id,
        square=db_platform.square,
        ceiling_height=db_platform.ceiling_height,
        closest_station=db_platform.closest_station,
        rent_type=db_platform.rent_type,
        price_per_time=db_platform.price_per_time,
        description=db_platform.description,
        geotag=db_platform.geotag,
        main_image=db_platform.main_image,
        platform_id=db_platform.platform_id,
        company_id=db_platform.company_id,
        images=[image.image for image in db_images]
    )
    return platform
