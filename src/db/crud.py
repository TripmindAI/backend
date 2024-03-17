from sqlalchemy.orm import Session
from . import models
from .. import schemas


def get_location_by_location_id(db: Session, location_id: str):
    return (
        db.query(models.Location)
        .filter(models.Location.location_id == location_id)
        .first()
    )


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


def get_user_by_auth0_sub(db: Session, auth0_sub: str):
    return db.query(models.User).filter(models.User.auth0_sub == auth0_sub).first()


def get_user_id_by_auth0_sub(db: Session, auth0_sub: str):
    return db.query(models.User.id).filter(models.User.auth0_sub == auth0_sub).first()


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def upsert_user(db: Session, user: schemas.UserCreate):

    user_id = get_user_id_by_auth0_sub(db, user.auth0_sub)
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        db_user = models.User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user


def toggle_like_location(db: Session, user_id: str, location_id: str):
    db_like_location = (
        db.query(models.user_likes_locations)
        .filter(user_id == user_id)
        .filter(location_id == location_id)
        .first()
    )
    if db_like_location:
        db.execute(
            models.user_likes_locations.delete().where(
                models.user_likes_locations.c.user_id == user_id,
                models.user_likes_locations.c.location_id == location_id,
            )
        )
        db.commit()
    else:
        db.execute(
            models.user_likes_locations.insert().values(
                user_id=user_id, location_id=location_id
            )
        )
        db.commit()


def get_liked_locations_for_user(db: Session, user_id: str):
    return (
        db.query(models.Location)
        .join(models.user_likes_locations)
        .filter(models.user_likes_locations.c.user_id == user_id)
        .all()
    )
