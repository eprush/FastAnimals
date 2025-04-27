"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

from website.external_api.foxes import get_randomfox_fox as get_fox
from website.external_api.cats import get_thecatapi_cat as get_cat
from website.external_api.dogs import get_dogapi_dog as get_dog204

animal_types = {name[4:] : func for name, func in globals().items() if name.startswith("get_")}
