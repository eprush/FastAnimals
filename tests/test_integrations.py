import pytest

from app.integrations.abstract_animal import AbstractAnimalReceiver
from app.integrations.common import AnimalReceiver
from app.integrations.real_animals import (
    DogReceiver,
    CatReceiver,
    FoxReceiver
)

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
    response = receiver.request_image()
    assert len(response) == 2
    assert type(response[0]) is str
    assert type(response[1]) is dict

def test_cannot_receive_unexistent_animal():
    common_receiver = AnimalReceiver()
    response = common_receiver.request_image("jaguar")
    assert response is None

