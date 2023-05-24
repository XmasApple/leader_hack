from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    user_id: Column = Column(Integer, primary_key=True, index=True)
    email: Column = Column(String, unique=True, index=True)
    hashed_password: Column = Column(String)
    first_name: Column = Column(String)
    last_name: Column = Column(String)
    middle_name: Column = Column(String)
    phone_number: Column = Column(String(11), unique=True, index=True)
