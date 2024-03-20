import os

def get_env_key(key_name : str):
    key = os.getenv(key_name)
    return key