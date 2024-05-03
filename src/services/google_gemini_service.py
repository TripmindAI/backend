# Description: This file contains the service for the OpenAI chat API.
import asyncio
from httpx import AsyncClient
import json
from ..schemas import RecommendationParameters
from ..utils.file_utils import get_env_key
from ..db import crud
from ..dependencies.database_dependencies import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


GEMINI_API_KEY = get_env_key("GEMINI_API_KEY")


headers = {
    "Content-Type": "application/json",
}


async def fetch_recommedations(parameters: RecommendationParameters):

    GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={GEMINI_API_KEY}"
    verb = "am" if parameters.people == "solo" else "are"
    pronoun = "I" if parameters.people == "solo" else "We"
    payload = json.dumps(
        {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": """
                            You are a tour guide. Please provide us with some recommendations for visiting different cities. 
                            Users will provide you with the name of a city. Please provide your suggestions for 3 different sites in this city, using JSON format. Additionally, please include a 
                            two-sentences description for each site along with its name.

                            Please use the following format (Your response will be directly used as an API response, directly fed 
                            into a program, to avoid the program crash, please only output the JSON part, do not add any other text):
                            [
                            {
                                "location_name": "xxx",
                                "location_id": "None",
                                "description": "xxxx",
                                "reason": "xxxx"
                            },
                            {
                                "location_name": "xxx",
                                "location_id": "None",
                                "description": "xxx",
                                "reason": "xxxx"
                            },
                            {
                                "location_name": "xxx",
                                "location_id": "None",
                                "description": "xxxx",
                                "reason": "xxxx"
                            }
                            ]
                            """
                            + f"\n\n{pronoun} {verb} planning to visit {parameters.city} and prefer {parameters.how_spend} attractions."
                        }
                    ],
                },
            ]
        }
    )

    async with AsyncClient(timeout=30.0) as client:
        response = await client.post(
            GEMINI_ENDPOINT,
            headers=headers,
            content=payload,
        )

    # Raise an exception if the call fails
    response.raise_for_status()
    data = response.json()


    # In FastAPI, this can be directly returned and will be converted to JSON
    return data


async def get_location_id(db, location_name: str):
    return await crud.get_location_by_name(db, location_name).location_id
