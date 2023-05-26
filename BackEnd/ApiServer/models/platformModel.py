from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint
from database import Base
from models.userModel import User

from models.userModel import User


class Platform(Base):
    __tablename__ = "platforms"

    platform_id: Column = Column(Integer, primary_key=True, index=True)
    name: Column = Column(String, unique=True, nullable=False)
    owner_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
    type: Column = Column(String)
    square: Column = Column(DECIMAL)
    ceiling_height: Column = Column(DECIMAL)
    closest_station: Column = Column(String)
    price_per_hour: Column = Column(DECIMAL, nullable=False)
    info: Column = Column(String)
