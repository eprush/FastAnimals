"""
Module implements getting random fox photo from external sources
"""

import requests
from random import randint


def get_randomfox_fox() -> bytes:
    fox_count = 124
    random_fox_number = randint(1, fox_count)
    headers = {"Content-Type": "application/json"}
    url = f"https://randomfox.ca//images//{random_fox_number}.jpg"
    return requests.get(url, headers= headers).content

if __name__ == "__main__":
    with open("img.jpg", "wb") as file:
        file.write(get_randomfox_fox())
