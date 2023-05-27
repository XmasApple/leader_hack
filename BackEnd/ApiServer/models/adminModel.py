from sqlalchemy import Column, Integer, ForeignKey
from database import Base, SessionLocal
from models.userModel import User


class Admin(Base):
    __tablename__ = "admins"

    admin_id: Column = Column(Integer, primary_key=True)
    user_id: Column = Column(Integer, ForeignKey(f"{User.__tablename__}.user_id"))

    @staticmethod
    def load_data():
        db = SessionLocal()
        if not db.query(Admin).count():
            db_user = db.query(User).filter(User.email == "admin").first()
            db_admin = Admin(user_id=db_user.user_id)
            db.add(db_admin)

            db.commit()
        db.close()
