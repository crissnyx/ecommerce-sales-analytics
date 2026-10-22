from datetime import datetime
from pydantic import BaseModel, Field
from backend.app.db.models import UploadStatus

class UploadCreate(BaseModel):
    original_filename: str = Field(..., min_length=1, max_length=255)

class UploadOut(BaseModel):
    id: int
    company_id: int
    user_id: int
    original_filename: str
    storage_filename: str
    storage_path: str
    file_size: int
    mime_type: str | None
    status: UploadStatus
    created_at: datetime
    processed_at: datetime | None = None

    class Config:
        from_attributes = True