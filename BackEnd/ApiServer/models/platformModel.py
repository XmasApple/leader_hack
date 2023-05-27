from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint
from database import Base
from models.userModel import User
from models.platformTypeModel import PlatformType


class Platform(Base):
    # Модель для карточки платформы
    __tablename__ = "platforms"
    __table_args__ = (
        CheckConstraint("rent_type in (1, 2)"),
        CheckConstraint("hidden_by_user in (0, 1)"),
        CheckConstraint("hidden_by_admin in (0, 1)"),
        CheckConstraint("is_verified in (0, 1)"),
    )

    platform_id: Column = Column(Integer, primary_key=True, index=True)
    name: Column = Column(String, unique=True, nullable=False)
    company_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"), nullable=False)
    platform_type_id: Column = Column(Integer,
                                      ForeignKey(f"{PlatformType.__tablename__}.platform_type_id"),
                                      nullable=False)
    square: Column = Column(DECIMAL)
    ceiling_height: Column = Column(DECIMAL)
    closest_station: Column = Column(String)
    people_capacity: Column = Column(Integer, nullable=False)
    # 1 - per hour, 2 - per day
    rent_type: Column = Column(Integer, nullable=False)
    price_per_time: Column = Column(DECIMAL, nullable=False)
    description: Column = Column(String)
    geotag: Column = Column(String)
    main_image: Column = Column(String)
    hidden_by_user = Column(Integer, nullable=False, default=0)
    hidden_by_admin = Column(Integer, nullable=False, default=0)
    is_verified = Column(Integer, nullable=False, default=0)

