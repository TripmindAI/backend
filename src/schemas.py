from pydantic import BaseModel, Field


class RecommendationParameters(BaseModel):
    city: str = Field(min_length=3, max_length=30)
    people: str
    how_spend: str


class LocationBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    city: str = Field(min_length=3, max_length=30)
    state: str = Field(min_length=3, max_length=30)
    country: str = Field(min_length=3, max_length=30)


class LocationCreate(LocationBase):
    description: str | None = Field(default=None, max_length=200)


class Location(LocationBase):
    id: int
    location_id: str
    web_url: str
    is_active: bool

    # Address information
    street1: str
    street2: str
    postalcode: str

    # Location data
    latitude: float
    longitude: float
    timezone: str

    class Config:
        orm_mode = True
