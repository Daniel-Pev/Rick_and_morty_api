"""
Rick and Motry.
Testing file
"""
import allure
import pytest
from pytest_voluptuous import S

from common.helper.schema.location import valid_location, error_location


@pytest.mark.location
@allure.feature('Location testing')
class TestLocation:
    """
    Test for character
    """
    CASES = [
        {'id': 1, 'status_code': 200, 'schema': valid_location},
        {'id': 126, 'status_code': 200, 'schema': valid_location},
        {'id': [1, 26, 35], 'status_code': 200, 'schema': valid_location},
        {'id': "1, 2, 3", 'status_code': 200, 'schema': valid_location},
        {'id': "1, -1, 3", 'status_code': 200, 'schema': valid_location},
        {'id': 827, 'status_code': 404, 'schema': error_location},
        {'id': -1, 'status_code': 404, 'schema': error_location},
        {'id': 1000, 'status_code': 404, 'schema': error_location},
        {'id': -1000, 'status_code': 404, 'schema': error_location},
        {'id': 'dwadadaw', 'status_code': 500, 'schema': error_location},
        {'id': '!@?&', 'status_code': 500, 'schema': error_location},

    ]

    @allure.story('Get Location')
    @pytest.mark.parametrize('case', CASES)
    def test_location(self, case, api_location):
        """
        Get character
        """
        response = api_location.get_location(location_id=case['id'])

        api_location.check_status_code(expected_code=case['status_code'])
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
