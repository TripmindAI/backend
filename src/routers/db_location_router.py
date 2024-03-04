from typing import Annotated
from fastapi import APIRouter, HTTPException, Query, status, Depends
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


@router.get("/get-location/{location_id}", response_model=schemas.Location)
def get_location(location_id: str, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_location_id(db, location_id)
    if db_location:
        return db_location
    raise HTTPException(status_code=404, detail="Location not found")


@router.get("/get-location/", response_model=schemas.Location)
def get_location(
    place: Annotated[
        str, Query(min_length=3, max_length=40, description="The name of the place")
    ],
    db: Session = Depends(get_db),
):
    db_location = crud.get_location_by_name(db=db, name=place)
    if db_location:
        return db_location
    raise HTTPException(status_code=404, detail="Location not found")
