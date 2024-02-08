from fastapi import FastAPI, Query, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field
from httpx import AsyncClient
import json

app = FastAPI()


OPENAI_API_KEY = "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"
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
url = "https://api.openai.com/v1/chat/completions"


class RecommendationParameters(BaseModel):
    city: str = Field(min_length=3, max_length=30)
    people: str
    how_spend: str


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/generate-recommedations/")
async def generate_recommedations(parameters: RecommendationParameters):
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

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())
