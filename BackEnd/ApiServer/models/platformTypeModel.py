from sqlalchemy import Column, Integer, String

<<<<<<< HEAD
from database import Base
=======
from database import Base, SessionLocal

PLATFORM_TYPES = [
    "Выставочные залы",
    "Художественные выставки / галереи",
    "Залы конференций ",
    "Залы для репетиций",
    "Фотостудии",
    "Корпоративные мероприятия",
    "Места для проведения совещаний",
    "Секонд Хенды",
    "Студии звукозаписи ",
    "На открытом воздухе",
    "Танцевальные студии",
    "Студии для креативного производства ",
    "Складские помещения",
]
>>>>>>> main


class PlatformType(Base):
    __tablename__ = "platform_types"

<<<<<<< HEAD
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
=======
    platform_type_id: Column = Column(Integer, primary_key=True, index=True)
    name: Column = Column(String, unique=True, nullable=False)

    # description = Column(String)

    @staticmethod
    def load_data():
        db = SessionLocal()
        if not db.query(PlatformType).count():
            # for platform_type in PLATFORM_TYPES:
            #     db.add(PlatformType(name=platform_type))
            db.add_all([PlatformType(name=platform_type) for platform_type in PLATFORM_TYPES])
            db.commit()
        db.close()
>>>>>>> main
