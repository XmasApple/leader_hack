from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

<<<<<<< HEAD
from database import engine, Base, get_db
from models import userModel, platformModel, bookingModel, adminModel
from routers import userRouter, platformRouter, bookingRouter, adminRouter
from crud import platformTypeCrud

models: list[Base] = [userModel, platformModel, bookingModel, adminModel]
=======
from database import engine
from models.all_models import models
from routers.all_routers import routers
>>>>>>> main

for model in models:
    model.metadata.create_all(bind=engine)
    # if method load_data exists in model
    if hasattr(model, "load_data"):
        model.load_data()

app = FastAPI()

<<<<<<< HEAD
routers: list = [userRouter, platformRouter, bookingRouter, adminRouter]

for router in routers:
    app.include_router(router.router)

platformTypeCrud.init_platform_types()
=======
for router in routers:
    app.include_router(router)
>>>>>>> main
