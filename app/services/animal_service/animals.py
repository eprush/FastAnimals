"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

from app.services.animal_service.dogs import get_dogapi_dog as get_dog
from app.services.animal_service.foxes import get_randomfox_fox as get_fox
from app.services.animal_service.cats import get_thecatapi_cat as get_cat

animal_types = {name[4:] : func for name, func in globals().items() if name.startswith("get_")}
