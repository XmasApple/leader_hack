from sqlalchemy import Column, Integer,  ForeignKey
from database import Base
from models.userModel import User


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
