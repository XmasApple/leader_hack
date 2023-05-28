from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base
from models.platformModel import Platform


class PlatformImage(Base):
    __tablename__ = "platform_images"

    platform_image_id: Column = Column(Integer, primary_key=True, index=True)
    platform_id: Column = Column(Integer, ForeignKey(f"{Platform.__tablename__}.platform_id"), index=True, nullable=False)
    image: Column = Column(String, nullable=False)  # base64
