from sqlalchemy.orm import Session
from . import models
from .. import schemas


def get_location_by_location_id(db: Session, location_id: str):
    return (
        db.query(models.Location)
        .filter(models.Location.location_id == location_id)
        .first()
    )


def get_location_by_id(db: Session, id: int):
    return db.query(models.Location).filter(models.Location.id == id).first()


def get_location_by_name(db: Session, name: str):
    return db.query(models.Location).filter(models.Location.name == name).first()


# get multiple locations
def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    db.refresh(db_location)
    return db_location
