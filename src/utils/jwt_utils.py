from authlib.jose import JsonWebToken
from authlib.jose import errors
from fastapi import Depends, HTTPException
from ..dependencies.token_dependencies import get_token
import os
from dotenv import load_dotenv, find_dotenv
from fastapi import Depends, HTTPException


crypto_algorithms = ["RS256"]
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InI4V3F2RDlLLTJ4azlHYnRiUHVxZiJ9.eyJnaXZlbl9uYW1lIjoiUkYiLCJmYW1pbHlfbmFtZSI6IlgiLCJuaWNrbmFtZSI6InhyZnhyZnhyZnhyZnhyZiIsIm5hbWUiOiJSRiBYIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tEbHVYbUozVDZ6VTdPTWN3SEhLRGpFN2h4Y3R1RVFGNFRtaHNpMGZGZD1zOTYtYyIsImxvY2FsZSI6InpoLUNOIiwidXBkYXRlZF9hdCI6IjIwMjQtMDMtMDNUMjA6MTM6NTAuMjEyWiIsImVtYWlsIjoieHJmeHJmeHJmeHJmeHJmQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL3RyaXBtaW5kYWkudXMuYXV0aDAuY29tLyIsImF1ZCI6IjhPeXl1THRBZFdmWlVhbzVLdk9qajFJUDlrZG4wZFBMIiwiaWF0IjoxNzA5NDk2ODMxLCJleHAiOjE3MDk1MzI4MzEsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2NDIyOTgwMDk5Mzg3NTcxNjk3Iiwic2lkIjoiQktUTFV4NUJnejZ6Q05zd2FzX2VjNS1QZzlHbEU3YkUiLCJub25jZSI6IjlvUzZxYzBBVWhPM0xpTjA0c0FKcnVkZi1HNElQZEY4eVJ1MjFhUjg0dEEifQ.KCiw7Ck83zB7aMqdeX5OC_IZE0zwnUsRTErb5qgkBU2DV8LAkD6iH4uWyUnTKCeQz7s63ZjUY1JalOjufKb9ASwdz176Icu3fhSikqc3phAcmHP1gyZfdwR3i-Wy8jUxYkP_PVUWovuKz-nX_hx-gi8PqOAX_8Do0TyMDO00mQPZdMscPFoGbR0cQoaKkkntGRjhO5WWJ82ltWXz61G6oJpX_a348Yw2CEbO4SMYyussXk995v9Q_EJWW7PquiAhK5N60kShiuTvDwfJWkjK6-oWPuat903i0cCiYrsweArB3_In-SszCGlVVoc3deUwjsh3m4DEcISmwUaCIqeHaQ"


def read_public_key():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    public_key_path = os.getenv("PUBLIC_KEY_PATH")
    if not public_key_path:
        raise ValueError("Public key path is not set")

    with open(public_key_path, "r") as file:
        return file.read()


def decode_and_verify_token(token: str = Depends(get_token)):
    try:
        public_key = read_public_key()
        jwt = JsonWebToken(crypto_algorithms)
        claims = jwt.decode(token, public_key)
        claims.validate()
        return claims
    except errors.DecodeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except errors.BadSignatureError:
        raise HTTPException(status_code=400, detail="Could not validate credentials")


def parse_clains(claims):
    return {
        "username": claims["name"],
        "email": claims["email"],
        "given_name": claims["given_name"],
        "family_name": claims["family_name"],
        "auth0_sub": claims["sub"],
        "profile_picture_url": claims["picture"],
        "updated_at": claims["updated_at"],
    }


# def read_file(filename):
#     with open(filename, "r") as file:
#         return file.read()


# def get_usr_info(token):

#     jwt = JsonWebToken(crypto_algorithms)
#     public_key = read_file("../publickey.pem")
#     claims = jwt.decode(token, public_key)
#     usr_info = parse_clains(claims)

#     return usr_info
