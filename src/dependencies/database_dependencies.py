# Dependency to get the database session
from ..db.database import SessionLocal
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

security = HTTPBearer()
def get_token(auth: HTTPAuthorizationCredentials = Depends(security)):
    return auth.credentials