"""
Module implements getting random dog photo from external sources
"""

import requests


def get_dogapi_dog() -> bytes:
    headers = {"Content-Type": "application/json"}
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url, headers= headers).json()
    image_link = response["message"]
    return requests.get(image_link, headers= headers).content
