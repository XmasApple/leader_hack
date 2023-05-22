from fastapi import FastAPI

from database import engine
from models.all_models import models
from routers.all_routers import routers

for model in models:
    model.metadata.create_all(bind=engine)
    # if method load_data exists in model
    if hasattr(model, "load_data"):
        model.load_data()

app = FastAPI()

for router in routers:
    app.include_router(router)
