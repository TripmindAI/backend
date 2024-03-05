import os
from dotenv import find_dotenv, load_dotenv

def get_env_key(key_name : str):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    key = os.getenv(key_name)
    return key