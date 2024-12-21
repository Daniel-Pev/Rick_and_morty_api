"""
Rick and Motry.
Testing file
"""
import allure
import pytest
from pytest_voluptuous import S

from common.helper.schema.character import valid_character, error_character


@pytest.mark.character
@allure.feature('Character testing')
class TestCharacter:
    """
    Test for character
    """
    CASES = [
        {'id': 1, 'status_code': 200, 'schema': valid_character},
        {'id': 826, 'status_code': 200, 'schema': valid_character},
        {'id': [1, 26, 35], 'status_code': 200, 'schema': valid_character},
        {'id': "1, 2, 3", 'status_code': 200, 'schema': valid_character},
        {'id': "0, -1, 3", 'status_code': 200, 'schema': valid_character},
        {'id': 827, 'status_code': 404, 'schema': error_character},
        {'id': -1, 'status_code': 404, 'schema': error_character},
        {'id': 1000, 'status_code': 404, 'schema': error_character},
        {'id': -1000, 'status_code': 404, 'schema': error_character},
        {'id': 'dwadadaw', 'status_code': 500, 'schema': error_character},
        {'id': '!@?&', 'status_code': 500, 'schema': error_character}

    ]

    @allure.story('Get Character')
    @pytest.mark.parametrize('case', CASES)
    def test_character(self, case, api_character):
        """
        Get character
        """
        response = api_character.get_character(character_id=case['id'])

        api_character.check_status_code(expected_code=case['status_code'])
        if not case['id']:
            for schema in response.response.json()[1:]:
                assert S(case['schema']) == schema
        if response.response.status_code >= 500:
            assert S(case['schema']) == response.response.json()
        elif not isinstance(case['id'], int):
            for schema in response.response.json():
                assert S(case['schema']) == schema
        else:
            assert S(case['schema']) == response.response.json()
