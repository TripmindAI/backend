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


OPENAI_API_KEY = get_env_key("OPENAI_API_KEY")


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}


async def fetch_recommedations(parameters: RecommendationParameters):

    openai_parameters = {
        "model": "gpt-3.5-turbo",
        "temperature": 1,
        "max_tokens": 1000,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,

    }
    OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    verb = "am" if parameters.people == "solo" else "are"
    pronoun = "I" if parameters.people == "solo" else "We"
    payload = json.dumps(
        {
            "model": openai_parameters["model"],
            "messages": [
                {
                    "role": "system",
                    "content": """
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

                                """,
                },
                {
                    "role": "user",
                    "content": f"{pronoun} {verb} planning to visit {parameters.city} and prefer {parameters.how_spend} attractions.",
                },
            ],
            "temperature": openai_parameters["temperature"],
            "max_tokens": openai_parameters["max_tokens"],
            "top_p": openai_parameters["top_p"],
            "frequency_penalty": openai_parameters["frequency_penalty"],
            "presence_penalty": openai_parameters["presence_penalty"],
        }
    )

    async with AsyncClient() as client:
        response = await client.post(
            OPENAI_ENDPOINT,
            headers=headers,
            content=payload,
        )

    # Raise an exception if the call fails
    response.raise_for_status()
    data = response.json()

    try:
        db = await get_db()
        tasks = [get_location_id(place["location_name"], db) for place in data]
        location_ids = await asyncio.gather(*tasks)

        for place, location_id in zip(data, location_ids):
            place["location_id"] = location_id  # Update location_id

    except Exception as e:  # Consider catching specific exceptions
        # Log the exception here for debugging
        return JSONResponse(
            content={"status": "error", "message": "An error occurred"}, status_code=500
        )

    # In FastAPI, this can be directly returned and will be converted to JSON
    return data


async def get_location_id(db, location_name: str):
    return await crud.get_location_by_name(db, location_name).location_id
