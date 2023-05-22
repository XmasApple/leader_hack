from fastapi import FastAPI

from database import engine, Base

from models import userModel, tokenModel, platformModel, bookingModel, companyModel, employeeModel
from routers import userRouter, platformRouter, bookingRouter, companyRouter

models: list[Base] = [userModel, tokenModel, platformModel, bookingModel, companyModel, employeeModel]

for model in models:
    model.Base.metadata.create_all(bind=engine)

app = FastAPI()

routers: list = [userRouter, platformRouter, bookingRouter, companyRouter]

for router in routers:
    app.include_router(router.router)
