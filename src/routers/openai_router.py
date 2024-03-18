# app/routers/openai_router.py
from fastapi import APIRouter, HTTPException
from ..services.openai_chat_service import fetch_recommedations
from ..schemas import RecommendationParameters
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/recommedations/")
async def get_recommendation(parameters: RecommendationParameters):
    try:
        recommendation = await fetch_recommedations(parameters)
        return recommendation
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code, content=e.detail
        )
