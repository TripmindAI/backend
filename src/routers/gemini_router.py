# app/routers/openai_router.py
from fastapi import APIRouter, HTTPException
from ..services.google_gemini_service import fetch_recommedations
from ..schemas import RecommendationParameters

router = APIRouter()

@router.post("/recommedations/")
async def get_recommendation(parameters: RecommendationParameters):
    try:
        recommendation = await fetch_recommedations(parameters)
        return recommendation
    except HTTPException as e:
        raise HTTPException(
            status_code=recommendation.status_code, detail=recommendation.json()
        )
