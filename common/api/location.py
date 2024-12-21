"""
Location endpoint
"""
import allure

from common.api.basic import Api


class LocationApi(Api):
    """
    Methods for location
    """

    def get_location(self, location_id=None, params=None):
        """
        Get location
        """
        with allure.step('get location by id'):
            if location_id:
                return self.get(url=f'{self.url}/location/{location_id}')
        with allure.step('get location by params'):
            return self.get(url=f'{self.url}/location', params=params)
