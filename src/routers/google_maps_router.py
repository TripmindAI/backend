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

        place_id_string = await fetch_place_ids(place)
        if place_id_string:
            place_id = json.loads(place_id_string)["places"][0]["id"]
            photo_id_string = await fetch_photo_ids(place_id)
            if photo_id_string:
                photo_id = json.loads(photo_id_string)["photos"][0]["name"]
                image_url = await fetch_photo_url(photo_id)
                return image_url

        return {
            "img_redirect_url": "https://placehold.co/600x400/000000/FFF?text=TripMind\nNo+Image+Found&font=Playfair%20Display"
        }

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)
