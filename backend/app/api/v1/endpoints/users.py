from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.api.deps import get_current_user, require_any_staff
from backend.app.db.models import User
from backend.app.db.session import get_db
from backend.app.schemas.user import UserOut

router = APIRouter()

@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[UserOut])
def list_users(
    current_user: User = Depends(require_any_staff),
    db: Session = Depends(get_db),
):
    return db.query(User).filter(User.company_id == current_user.company_id).all()

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(
    user_id: int,
    current_user: User = Depends(require_any_staff),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id, User.company_id == current_user.company_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user