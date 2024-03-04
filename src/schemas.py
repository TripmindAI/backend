from pydantic import BaseModel, Field, validator
import pycountry
from zoneinfo import ZoneInfo, available_timezones
from uuid import UUID
from datetime import datetime


class RecommendationParameters(BaseModel):
    city: str = Field(min_length=3, max_length=30)
    people: str
    how_spend: str


class LocationBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    state: str = Field(min_length=3, max_length=30)
    country: str = Field(min_length=3, max_length=60)

    @validator("country")
    def country_exists(cls, v):
        try:
            pycountry.countries.lookup(v)
        except LookupError:
            raise ValueError(f"{v} is not a valid ISO 3166 country code")
        return v


class LocationCreate(LocationBase):

    city: str | None = Field(default=None, min_length=3, max_length=30)
    description: str | None = Field(default=None, max_length=500)


class Location(LocationBase):
    city: str | None = Field(default=None, min_length=3, max_length=30)
    description: str | None = Field(default=None, max_length=500)
    id: int
    location_id: UUID
    web_url: str | None = None
    is_active: bool
    create_at: datetime

    # Address information
    street1: str | None = None
    street2: str | None = None
    postalcode: str | None = None

    # Location data
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)
    timezone: str | None = None

    @validator("timezone")
    def timezone_exists(cls, v):
        if v and v not in available_timezones():
            raise ValueError(f"{v} is not a valid timezone")
        return v

    class Config:
        from_attributes = True
        json_encoders = {
            UUID: lambda v: str(v),  # Convert UUID to str when serializing to JSON
            datetime: lambda v: v.isoformat(),  # Ensure datetime is ISO-formatted string
        }
