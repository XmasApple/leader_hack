from pydantic import BaseModel


class PlatformFeedbackBase(BaseModel):
    platform_id: int
    rating: int
    feedback: str


class PlatformFeedbackCreate(PlatformFeedbackBase):
    pass


class PlatformFeedback(PlatformFeedbackBase):
    platform_feedback_id: int

    class Config:
        orm_mode = True
