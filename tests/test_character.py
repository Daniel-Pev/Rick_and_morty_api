"""
Rick and Motry.
Testing file
"""

import pytest
from pytest_voluptuous import S

from common.helper.schema.trainer import valid_character, error_character


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
        {'id': 'ya_pes', 'status_code': 500, 'schema': error_character},

    ]

    @pytest.mark.parametrize('case', CASES)
    def test_character(self, case, api):
        """
        Get character
        """
        response = api.get_character(character_id=case['id'])

        api.check_status_code(expected_code=case['status_code'])
        if not isinstance(case['id'], int):
            for schema in response.response.json():
                assert S(case['schema']) == schema
        else:
            assert S(case['schema']) == response.response.json()
