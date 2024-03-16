# app/main.py
from fastapi import FastAPI
from .routers import google_maps_router, location_router, openai_router, account_rounter

app = FastAPI()

#Include the routers from the routers folder
app.include_router(openai_router.router, prefix="/v1/backend-api/openai", tags=["OpenAI"])
app.include_router(google_maps_router.router, prefix="/v1/backend-api/google-maps", tags=["Google Maps"])
app.include_router(location_router.router, prefix="/v1/backend-api/locations", tags=["Locations"])
app.include_router(account_rounter.router, prefix="/v1/accounts", tags=["DB Opearations"])