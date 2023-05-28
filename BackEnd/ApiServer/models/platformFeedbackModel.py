from sqlalchemy import Column, Integer, String, ForeignKey

import models.all_models as models
from database import Base


class PlatformFeedback(Base):
    __tablename__ = "platform_feedbacks"

    platform_feedback_id: Column = Column(Integer, primary_key=True)
    platform_id: Column = Column(Integer, ForeignKey(f"{models.User.__tablename__}.user_id"), index=True, nullable=False)
    rating: Column = Column(Integer, nullable=False)
    feedback: Column = Column(String)
