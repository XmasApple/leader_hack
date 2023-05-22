from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from models.userModel import User


class Token(Base):
    __tablename__ = "user_tokens"

    token_id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))
    expire_date = Column(Integer)
