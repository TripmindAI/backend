from pydantic import BaseModel, Field, validator
import pycountry
from zoneinfo import ZoneInfo, available_timezones


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

    city: str | None =  Field(default=None, min_length=3, max_length=30)
    description: str | None = Field(default=None, max_length=200)


class Location(LocationBase):
    id: int
    location_id: str
    web_url: str
    is_active: bool
    create_at: str

    # Address information
    street1: str
    street2: str
    postalcode: str

    # Location data
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    timezone: str

    @validator("timezone")
    def timezone_exists(cls, v):
        if v not in available_timezones():
            raise ValueError(f"{v} is not a valid timezone")
        return v

    class Config:
        orm_mode = True
