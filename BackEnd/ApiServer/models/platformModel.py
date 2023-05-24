from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint
from database import Base
from models.userModel import User

from models.userModel import User


class Platform(Base):
    __tablename__ = "platforms"

<<<<<<< HEAD
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
=======
    platform_id: Column = Column(Integer, primary_key=True, index=True)
    name: Column = Column(String, unique=True, nullable=False)
    owner_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
    # Думаю, в случае с типом площадки правильным решением будет
    # определить, какие площадки вообще могут быть и написать
    # под них Enum. Обсудим на созвоне.
    type: Column = Column(String)
    square: Column = Column(DECIMAL)
    ceiling_height: Column = Column(DECIMAL)
    closest_station: Column = Column(String)
    price_per_hour: Column = Column(DECIMAL, nullable=False)
    info: Column = Column(String)
>>>>>>> main
