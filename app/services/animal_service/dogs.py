"""
Module implements getting random dog photo from external sources
"""

import requests


def get_dogapi_dog() -> tuple[str, dict]:
    headers = {"Content-Type": "application/json"}
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url, headers= headers).json()
    dog_link = response.get("message", None) if response else None
    return dog_link, headers
