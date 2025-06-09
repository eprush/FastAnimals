import pytest
import requests

from app.integrations.abstract_animal import AbstractAnimalReceiver
from app.integrations.common import AnimalReceiver
from app.integrations.real_animals import (
    DogReceiver,
    CatReceiver,
    FoxReceiver
)

@pytest.fixture(scope="module")
def common_receiver():
    return AnimalReceiver()

def test_cannot_create_abstract_animal_receiver():
    with pytest.raises(TypeError):
        AbstractAnimalReceiver()

@pytest.mark.parametrize("receiver", (
        DogReceiver(),
        CatReceiver(),
        FoxReceiver(),
    )
)
def test_api_response(receiver):
    my_response = receiver.request_image()
    assert len(my_response) == 2
    assert type(my_response[0]) is str
    assert type(my_response[1]) is dict
    api_response = requests.get(my_response[0], headers=dict(my_response[1]))
    assert api_response.status_code == 200
    assert type(api_response.content) is bytes

def test_cannot_receive_unexistent_animal(common_receiver):
    response = common_receiver.request_image("jaguar")
    assert response is None

