from sqlalchemy import Column, Integer, String

from database import Base, SessionLocal

PLATFORM_TYPES = [
    "Киностудии",
    "Галереи",
    "Издательства",
    "Книжные магазины",
    "Выставочные залы",
    "Дизайн студии",
    "Креативные пространства",
    "Кинотеатры",
    "Звукозаписывающие студии",
    "Танцевальная студия",
    "AR/VR студии",
]


class PlatformType(Base):
    __tablename__ = "platform_types"

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
