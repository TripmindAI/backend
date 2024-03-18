from httpx import AsyncClient
from ..utils.file_utils import get_env_key
import json
from fastapi.responses import JSONResponse

GOOGLE_MAPS_API_KEY = get_env_key("GOOGLE_MAPS_API_KEY")


async def fetch_place_ids(place: str):
    GOOGLE_MAPS_Search_Place_ENDPOINT = (
        "https://places.googleapis.com/v1/places:searchText"
    )
    payload = json.dumps({"textQuery": place})
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "places.id",
    }
    async with AsyncClient() as client:
        response = await client.post(
            GOOGLE_MAPS_Search_Place_ENDPOINT, content=payload, headers=headers
        )

    # Raise an exception if the call fails
    try:
        response.raise_for_status()
        data = response.read()
        return data.decode("utf-8")
    except Exception as e:
        return None


async def fetch_photo_ids(place_id: str):
    GOOGLE_MAPS_Place_Details_ENDPOINT = (
        f"https://places.googleapis.com/v1/places/{place_id}?languageCode=en"
    )

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "id,displayName,photos",
    }
    async with AsyncClient() as client:
        response = await client.get(GOOGLE_MAPS_Place_Details_ENDPOINT, headers=headers)

    # Raise an exception if the call fails
    try:
        response.raise_for_status()
        data = response.read()
        return data.decode("utf-8")
    except Exception as e:
        return None


async def fetch_photo_url(photo_id: str):
    max_height_px = 600
    max_width_px = 600
    image_url = f"https://places.googleapis.com/v1/{photo_id}/media?maxHeightPx={max_height_px}&maxWidthPx={max_width_px}&key={GOOGLE_MAPS_API_KEY}"
    image_url = await get_redirect_url(image_url)
    return image_url


async def get_redirect_url(url: str):

    async with AsyncClient(follow_redirects=False) as client:
        response = await client.get(url)

        # Check if the response status code indicates a redirect
        if response.status_code in (301, 302, 303, 307, 308):
            return {"img_redirect_url": response.headers.get("Location")}
        else:
            return {"img_redirect_url": "https://placehold.co/600x400/000000/FFF?text=TripMind\nNo+Image+Found&font=Playfair%20Display"}
