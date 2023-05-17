from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from database import Base


class Platform(Base):
    # Модель для карточки платформы
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # Думаю, в случае с типом площадки правильным решением будет
    # определить, какие площадки вообще могут быть и написать
    # под них Enum. Обсудим на созвоне.
    type = Column(String)
    square = Column(DECIMAL)
    ceiling_height = Column(DECIMAL)
    closest_station = Column(String)
    price_per_hour = Column(DECIMAL, nullable=False)
    info = Column(String)