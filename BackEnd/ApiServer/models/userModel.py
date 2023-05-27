import hashlib

from sqlalchemy import Column, Integer, String
from database import Base, SessionLocal


class User(Base):
    __tablename__ = "users"

    user_id: Column = Column(Integer, primary_key=True, index=True)
    email: Column = Column(String, unique=True, index=True)
    hashed_password: Column = Column(String)
    first_name: Column = Column(String)
    last_name: Column = Column(String)
    middle_name: Column = Column(String)
    phone_number: Column = Column(String(11), unique=True, index=True)

    @staticmethod
    def load_data():
        db = SessionLocal()
        if not db.query(User).count():
            h = hashlib.sha256()
            h.update("admin".encode('utf-8'))
            hashed_password = h.hexdigest()
            # db.add_all([PlatformType(name=platform_type) for platform_type in PLATFORM_TYPES])
            db_admin = User(
                email="admin",
                hashed_password=hashed_password,
                first_name="admin",
                last_name="admin",
                middle_name="admin",
                phone_number="71112221234",
            )
            db.add(db_admin)
            db.commit()
        db.close()
