import os
from dotenv import load_dotenv
from functools import wraps

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        load_dotenv("./.env")
        api_key = os.getenv("RIOT_API_KEY")

        if api_key is None:
            api_key = input("Please provide the RIOT_API_KEY: ")

        return func(*args, **kwargs, api_key=api_key)
    return wrapper

# Use the decorator on a function
@require_api_key
def example_func(api_key):
    print(f"Got API key: {api_key}")