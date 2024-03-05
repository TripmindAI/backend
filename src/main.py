# app/main.py
from fastapi import FastAPI
from .routers import google_maps_router, openai_router, db_location_router, account_rounter

app = FastAPI()

#Include the routers from the routers folder
app.include_router(openai_router.router, prefix="/v1/backend-api/openai", tags=["OpenAI"])
app.include_router(google_maps_router.router, prefix="/v1/backend-api/google-maps", tags=["Google Maps"])
app.include_router(db_location_router.router, prefix="/v1/backend-api/locations", tags=["DB Opearations"])
app.include_router(account_rounter.router, prefix="/v1/backend-api/accounts", tags=["DB Opearations"])