"""
Conftest file
"""
import pytest

from common.api.character import CharacterApi
from common.api.location import LocationApi


@pytest.fixture
def api_character():
    """
    basic api fixture
    """
    my_api = CharacterApi()
    yield my_api


@pytest.fixture
def api_location():
    """
    basic api fixture
    """
    my_api = LocationApi()
    yield my_api
