from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy import ForeignKey, CheckConstraint

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Platform(Base):
    # Модель для карточки платформы
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    # Думаю, в случае с типом площадки правильным решением будет
    # определить, какие площадки вообще могут быть и написать
    # под них Enum. Обсудим на созвоне.
    type = Column(String)
    square = Column(DECIMAL)
    ceiling_height = Column(DECIMAL)
    closest_station = Column(String)
    price_per_hour = Column(DECIMAL, nullable=False)
    info = Column(String)
    # TODO: контакты владельца
    price_per_hour = Column(Integer)

class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    number_of_persons = Column(Integer)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

class Owner(User):
    __tablename__ = "owners"
    
    telephone = Column(String, CheckConstraint("LEN(telephone) = 20"))