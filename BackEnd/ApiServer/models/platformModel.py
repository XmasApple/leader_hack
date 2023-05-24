from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint
from database import Base

from models.userModel import User


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
    type = Column(String)
    square = Column(DECIMAL)
    ceiling_height = Column(DECIMAL)
    closest_station = Column(String)
    price_per_hour = Column(DECIMAL, nullable=False)
    info = Column(String)
    hidden_by_admin = Column(Integer, CheckConstraint("hidden_by_admin <=1 AND hidden_by_admin >= 0"))
    hidden_by_user = Column(Integer, CheckConstraint("hidden_by_user <=1 AND hidden_by_user >= 0"))
