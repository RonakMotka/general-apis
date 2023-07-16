from pydantic import BaseModel, Field



class MailDetail(BaseModel):
    to_email: str = Field(..., min_length=5, max_length=60)
    title: str = Field(..., min_length=2, max_length=60)
    subject: str = Field(..., min_length=2, max_length=100)
    template: str