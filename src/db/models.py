# SQLAlchemy models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index = True, nullable=False)
    web_url = Column(String)
    is_active = Column(Boolean, default=True)

    # Address information
    street1 = Column(String)
    street2 = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postalcode = Column(String)

    # Location data
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String)