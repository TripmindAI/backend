from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from ..services.google_maps_service import (
    fetch_place_ids,
    fetch_photo_ids,
    fetch_photo_url,
)
from typing import Annotated
import json


router = APIRouter()


@router.get("/images/")
async def get_maps_image(
    place: Annotated[
        str, Query(min_length=3, max_length=40, description="The name of the place")
    ]
):
    try:

        place_id = json.loads(await fetch_place_ids(place))["places"][0]["id"]
        if place_id:
            photo_id = json.loads(await fetch_photo_ids(place_id))["photos"][0]["name"]
            if photo_id:
                image_url = await fetch_photo_url(photo_id)
                return image_url

        return {"img_redirect_url": "https://placehold.co/600x400/000000/FFF?text=TripMind\nNo+Image+Found&font=Playfair%20Display"}

    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code, content=e.detail
        )

