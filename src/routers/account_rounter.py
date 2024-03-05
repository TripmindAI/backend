from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..utils.jwt_utils import decode_and_verify_token, parse_clains
from ..dependencies.database_dependencies import get_db
from ..db import crud

router = APIRouter()
@router.get("/auth/login")
async def user_login(claims: dict = Depends(decode_and_verify_token), db: Session = Depends(get_db)):
    try:
        print(claims)
        user_info = parse_clains(claims)
        print(user_info)
        # db_user = crud.upsert_user(db, schemas.UserCreate(**user_info))
        # return db_user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))