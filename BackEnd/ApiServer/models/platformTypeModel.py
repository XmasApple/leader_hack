from sqlalchemy import Column, Integer, String

from database import Base


class PlatformType(Base):
    __tablename__ = "platform_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
