from typing import Annotated
from fastapi import APIRouter, HTTPException, Query, status, Depends

from ..utils.jwt_utils import decode_and_verify_token, parse_claims
from .. import schemas
from ..db import crud
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..dependencies.database_dependencies import get_db

router = APIRouter()


@router.post("/location/", response_model=schemas.Location)
def add_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    # Attempt to get the location by name to check if it already exists.
    db_location = crud.get_location_by_name(db, location.name)
    if db_location:
        # If the location exists, raise a 400 Bad Request exception.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Location {location.name} already exists.",
        )

    # Try to create the location since it doesn't exist.
    db_location = crud.create_location(db=db, location=location)
    if not db_location:
        # If the location couldn't be created for some reason, raise a 400 Bad Request exception.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Location could not be created.",
        )
    # If the location was successfully created, return it.
    return db_location


@router.get("/location/{location_id}", response_model=schemas.Location)
def get_location(location_id: str, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_location_id(db, location_id)
    if db_location:
        return db_location
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Location not found"
    )


@router.get("/location/", response_model=schemas.Location)
def get_location(
    place: Annotated[
        str, Query(min_length=3, max_length=40, description="The name of the place")
    ],
    db: Session = Depends(get_db),
):
    db_location = crud.get_location_by_name(db=db, name=place)
    if db_location:
        return db_location
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Location not found"
    )


@router.post("/location/likes/{location_id}")
def toggle_like_location(location_id: str, token: str, db: Session = Depends(get_db)):
    try:
        claims = parse_claims(decode_and_verify_token(token))
        auth0_sub = claims["sub"]
        user_id = crud.get_user_id_by_auth0_sub(db, auth0_sub)
        liked = crud.toggle_like_location(db, user_id, location_id)
        if liked:
            return {"status": "liked"}
        return {"status": "unliked"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
