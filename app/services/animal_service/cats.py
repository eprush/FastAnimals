"""
Module implements getting random cat photo from external sources
"""

import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = str(os.getenv("CAT_API_KEY"))
def get_thecatapi_cat() -> tuple[str, dict]:
    headers = {"Content-Type": "application/json", "api_key": api_key}
    url = f"https://api.thecatapi.com/v1/images/search"
    response = requests.get(url, headers= headers).json()
    cat_link = response[0].get("url", None) if response else None
    return cat_link, headers
