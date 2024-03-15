from fastapi import APIRouter, HTTPException, Query
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
        photo_id = json.loads(await fetch_photo_ids(place_id))["photos"][0]["name"]
        image_url = await fetch_photo_url(photo_id)

        return image_url

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.Message)
