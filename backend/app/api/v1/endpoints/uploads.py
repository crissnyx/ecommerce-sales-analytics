from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from backend.app.api.deps import require_any_staff
from backend.app.core.config import UPLOADS_DIR
from backend.app.db.models import Upload, UploadStatus, User
from backend.app.db.session import get_db
from backend.app.schemas.upload import UploadOut

router = APIRouter()

@router.post("/", response_model=UploadOut, status_code=status.HTTP_201_CREATED)
def create_upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_any_staff),
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="File name is required")
    
    allowed_extensions = {".csv", ".xlsx", ".xls"}
    suffix = Path(file.filename).suffix.lower()
    if suffix not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Only CSV/XLS/XLSX file uploads are allowed")
    
    storage_name = f"{uuid4()}_{file.filename}"
    storage_path = UPLOADS_DIR / str(current_user.company_id) / storage_name
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    
    contents = file.file.read()
    storage_path.write_bytes(contents)
    
    upload = Upload(
        company_id=current_user.company_id,
        user_id=current_user.id,
        original_filename=file.filename,
        storage_filename=storage_name,
        storage_path=str(storage_path),
        file_size=len(contents),
        mime_type=file.content_type,
        status=UploadStatus.PENDING,
    )
    db.add(upload)
    db.commit()
    db.refresh(upload)
    return upload

@router.get("/", response_model=list[UploadOut])
def list_uploads(
    current_user: User = Depends(require_any_staff),
    db: Session = Depends(get_db),
):
    return db.query(Upload).filter(Upload.company_id == current_user.company_id).order_by(Upload.created_at.desc()).all()

@router.get("/{upload_id}", response_model=UploadOut)
def get_upload_by_id(
    upload_id: int,
    current_user: User = Depends(require_any_staff),
    db: Session = Depends(get_db),
):
    upload = db.query(Upload).filter(Upload.id == upload_id, Upload.company_id == current_user.company_id).first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Upload not found")
    return upload