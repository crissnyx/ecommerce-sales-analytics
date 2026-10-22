from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from backend.app.core.security import create_access_token, get_password_hash, verify_password
from backend.app.db.models import Company, User
from backend.app.db.session import get_db
from backend.app.schemas.user import Token, UserCreate, UserLogin, UserOut

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    company = None
    if payload.company_name:
        company = db.query(Company).filter(Company.name == payload.company_name).first()
        if company is None:
            company = Company(name=payload.company_name, plan="starter")
            db.add(company)
            db.commit()
            db.refresh(company)
    else:
        company = db.query(Company).filter(Company.name == "Default Company").first()
        if not company:
            company = Company(name="Default Company", plan="starter")
            db.add(company)
            db.commit()
            db.refresh(company)

    user = User(
        company_id=company.id,
        email=payload.email,
        password_hash=get_password_hash(payload.password),
        full_name=payload.full_name,
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login_user(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    
    access_token = create_access_token(
        subject=user.email,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}