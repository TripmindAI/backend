# Description: This file contains the service for the OpenAI chat API.
from httpx import AsyncClient
import json
from ..schemas import RecommendationParameters
from ..utils.file_utils import get_env_key
from fastapi.responses import JSONResponse


OPENAI_API_KEY = get_env_key("OPENAI_API_KEY")


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}


async def fetch_recommedations(parameters: RecommendationParameters):
    # OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    # OPENAI_ENDPOINT = "https://api.ohmygpt.com/v1/chat/completions"
    OPENAI_ENDPOINT = "https://gateway.ai.cloudflare.com/v1/29dcd52eab6f2de2b544e6b9d8c55dc1/tripmind-openai/openai/chat/completions"
    verb = "am" if parameters.people == "solo" else "are"
    pronoun = "I" if parameters.people == "solo" else "We"
    payload = json.dumps(
        {
            "model": "gpt-3.5-turbo-0125",
            "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": """
                                    You are a tour guide. Please provide us with some recommendations for visiting different cities. 
                                    Users will provide you with the name of a city. Please provide your suggestions for from 5 to 10 different sites in this city, using JSON format. Additionally, please include a 
                                    concise but useful two-sentences description and reason for each site along with its name.

                                    Please use the following format (Your response will be directly used as an API response, directly fed 
                                    into a program, to avoid the program crash, please only output the JSON part, do not add any other text):

                                    {
                                    "site": [
                                        {
                                        "Place Name": "Place1",
                                        "Description": "xxx",
                                        "Reason": "xxxx"
                                        },
                                        {
                                        "Place Name": "Place2",
                                        "Description": "xxx",
                                        "Reason": "xxxx"
                                        },
                                        {
                                        "Place Name": "Place3",
                                        "Description": "xxx",
                                        "Reason": "xxxx"
                                        }
                                    ]
                                    }
                                """,
                },
                {
                    "role": "user",
                    "content": f"{pronoun} {verb} planning to visit {parameters.city} and prefer {parameters.how_spend} attractions.",
                },
            ],
            "temperature": 1,
            "max_tokens": 4095,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        }
    )

    async with AsyncClient(timeout=60.0) as client:
        response = await client.post(
            OPENAI_ENDPOINT,
            headers=headers,
            content=payload,
        )

    # Raise an exception if the call fails

    try:
        response.raise_for_status()
        return response.json()
    except Exception as e:
        response_data = e.response.json()
        status_code = response_data.pop("statusCode", 400)
        return JSONResponse(content=response_data, status_code=status_code)

