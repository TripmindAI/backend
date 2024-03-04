from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas
from ..db import crud
from sqlalchemy.orm import Session
from ..db.database import SessionLocal

router = APIRouter()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add-location/", response_model=schemas.Location)
def add_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    db_location = crud.create_location(db=db, location=location)
    if db_location:
        return db_location
    raise HTTPException(status_code=400, detail="Location could not be created")
