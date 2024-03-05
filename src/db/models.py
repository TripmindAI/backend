# SQLAlchemy models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import ENUM
from ..utils.enums import UserRole, UserStatus

from .database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(UUID(as_uuid=True), unique=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, index = True, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    web_url = Column(String)
    is_active = Column(Boolean, default=True)
    description = Column(String)

    # Address information
    street1 = Column(String)
    street2 = Column(String)
    city = Column(String)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postalcode = Column(String)

    # Location data
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), unique=True, index=True, nullable=False, default=uuid.uuid4)
    user_name = Column(String, index=True, nullable=False)
    profile_picture_url = Column(String)
    auth0_sub = Column(String, nullable=False)
    email = Column(String, nullable=False)
    given_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
    status = Column(ENUM(UserStatus), default=UserStatus.ACTIVE, nullable=False)
    role = Column(ENUM(UserRole), default=UserRole.FREE, nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=False)


