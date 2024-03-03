from pydantic import BaseModel, Field


class RecommendationParameters(BaseModel):
    city: str = Field(min_length=3, max_length=30)
    people: str
    how_spend: str

class LocationBase(BaseModel):
    location_id: str
    name: str

class LocationCreate(LocationBase):
    description: str = ""

class Location(LocationBase):
    id: int
    web_url: str
    is_active: bool

    # Address information
    street1: str
    street2: str
    city: str
    state: str
    country: str
    postalcode: str

    # Location data
    latitude: float
    longitude: float
    timezone: str

    class Config:
        orm_mode = True

        
