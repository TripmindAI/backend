# Description: This file contains the service for the OpenAI chat API.
from httpx import AsyncClient
import json
from ..models import RecommendationParameters


OPENAI_API_KEY = "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"


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}


async def fetch_recommedations(parameters: RecommendationParameters):
    OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    verb = "am" if parameters.people == "solo" else "are"
    pronoun = "I" if parameters.people == "solo" else "We"
    payload = json.dumps(
        {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": """
                                    You are a tour guide. Please provide us with some recommendations for visiting different cities. 
                                    Users will provide you with the name of a city. Please provide your suggestions for a minimum of 3 
                                    and a maximum of 5 different sites in this city, using JSON format. Additionally, please include a 
                                    two-sentences description for each site along with its name.

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
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
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

    return response.json()
