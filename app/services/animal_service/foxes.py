"""
Module implements getting random fox photo from external sources
"""

from random import randint


def get_randomfox_fox() -> tuple[str, dict]:
    fox_count = 124
    random_fox_number = randint(1, fox_count)
    headers = {"Content-Type": "application/json"}
    fox_link = f"https://randomfox.ca//images//{random_fox_number}.jpg"
    return fox_link, headers
