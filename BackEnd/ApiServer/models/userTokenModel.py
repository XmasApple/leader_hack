from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from models.userModel import User


class UserToken(Base):
    __tablename__ = "user_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
    expire_date = Column(Integer)
