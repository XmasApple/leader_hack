from fastapi import FastAPI

from database import engine, Base
from models import userModel, platformModel, bookingModel
from routers import userRouter, platformRouter, bookingRouter

models: list[Base] = [userModel, platformModel, bookingModel]

for model in models:
    model.Base.metadata.create_all(bind=engine)

app = FastAPI()

routers: list = [userRouter, platformRouter, bookingRouter]

for router in routers:
    app.include_router(router.router)
