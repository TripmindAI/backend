# app/main.py
from fastapi import FastAPI
from .routers import google_maps_router, openai_router, db_location_router

app = FastAPI()

#Include the routers from the routers folder
app.include_router(openai_router.router, prefix="/backend-api/openai", tags=["OpenAI"])
app.include_router(google_maps_router.router, prefix="/backend-api/google-maps", tags=["Google Maps"])
app.include_router(db_location_router.router, prefix="/db-api", tags=["DB Opearations"])