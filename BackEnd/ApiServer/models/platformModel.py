from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from database import Base
from models.userModel import User


class Platform(Base):
    # Модель для карточки платформы
    __tablename__ = "platforms"

    platform_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
    # Думаю, в случае с типом площадки правильным решением будет
    # определить, какие площадки вообще могут быть и написать
    # под них Enum. Обсудим на созвоне.
    type = Column(String)
    square = Column(DECIMAL)
    ceiling_height = Column(DECIMAL)
    closest_station = Column(String)
    price_per_hour = Column(DECIMAL, nullable=False)
    info = Column(String)
