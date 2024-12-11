"""
Conftest file
"""
import pytest

from common.api.character import CharacterApi


@pytest.fixture
def api():
    """
    basic api fixture
    """
    my_api = CharacterApi()
    yield my_api
