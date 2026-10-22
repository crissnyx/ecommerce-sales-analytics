from datetime import datetime
from pydantic import BaseModel, Field

class CompanyCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    plan: str = "starter"

class CompanyOut(BaseModel):
    id: int
    name: str
    plan: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True