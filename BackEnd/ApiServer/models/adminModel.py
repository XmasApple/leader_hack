from sqlalchemy import Column, Integer,  ForeignKey
from database import Base
from models.userModel import User


class Admin(Base):
    __tablename__ = "admins"

    id: Column = Column(Integer, primary_key=True)
    user_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
