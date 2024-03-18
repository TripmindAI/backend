from authlib.jose import JsonWebToken
from authlib.jose import errors
from fastapi import Depends, HTTPException
from ..dependencies.token_dependencies import get_token
from fastapi import Depends, HTTPException
from .file_utils import get_env_key
from fastapi.responses import JSONResponse


ALGORITHMS = ["RS256"]

def read_public_key():
    public_key_path = get_env_key("PUBLIC_KEY_PATH")
    if not public_key_path:
        return JSONResponse(
            status_code=400, content={"message": "Public key path is not set"}
        )

    with open(public_key_path, "r") as file:
        return file.read()


def decode_and_verify_token(token: str = Depends(get_token)):
    try:
        public_key = read_public_key()
        jwt = JsonWebToken(ALGORITHMS)
        claims = jwt.decode(token, public_key)
        claims.validate()
        return claims
    except errors.JoseError as e:
        return JSONResponse(
            status_code=400, content={"message": f"Token is not valid: {e}"}
        )

def parse_claims(claims):
    return {
        "username": claims["name"],
        "email": claims["email"],
        "given_name": claims["given_name"],
        "family_name": claims["family_name"],
        "auth0_sub": claims["sub"],
        "profile_picture_url": claims["picture"],
        "updated_at": claims["updated_at"],
    }