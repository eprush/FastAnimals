from fastapi import FastAPI

from .external_api.animals import animal_types
from .external_api.utils import save_image


app = FastAPI()

@app.get("/")
def read():
    return {"Hello": "World"}

@app.get("/animal/{animal_type}")
def read_fox(animal_type: str):
    func = animal_types[animal_type]
    animal = func()
    save_image(animal)
    return {}
