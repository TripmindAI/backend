from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..utils.jwt_utils import decode_and_verify_token, parse_claims
from ..dependencies.database_dependencies import get_db
from ..db import crud
from fastapi.responses import JSONResponse

router = APIRouter()
@router.get("/auth/login", response_model=schemas.User)
async def user_login(claims: dict = Depends(decode_and_verify_token), db: Session = Depends(get_db)):
    try:
        user_info = parse_claims(claims)
        db_user = crud.upsert_user(db, schemas.UserCreate(**user_info))
        return db_user
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"User is not found: {e}"}
        )