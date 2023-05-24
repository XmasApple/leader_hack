from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import userModel, platformModel, bookingModel, adminModel
from routers import userRouter, platformRouter, bookingRouter, adminRouter
from crud import platformTypeCrud

models: list[Base] = [userModel, platformModel, bookingModel, adminModel]

for model in models:
    model.Base.metadata.create_all(bind=engine)

app = FastAPI()

routers: list = [userRouter, platformRouter, bookingRouter, adminRouter]

for router in routers:
    app.include_router(router.router)

platformTypeCrud.init_platform_types()
