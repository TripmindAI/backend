# app/main.py
from fastapi import FastAPI
from .routers import google_maps_router, openai_router

app = FastAPI()

#Include the routers from the routers folder
app.include_router(openai_router.router, prefix="/openai", tags=["OpenAI"])
app.include_router(google_maps_router.router, prefix="/google-maps", tags=["Google Maps"])