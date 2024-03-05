from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


def get_token(auth: HTTPAuthorizationCredentials = Depends(security)):
    return auth.credentials
