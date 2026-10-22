from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from backend.app.db.models import Role

class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=255)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)
    company_name: str | None = None
    role: Role = Role.VIEWER

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int
    company_id: int
    role: Role
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"