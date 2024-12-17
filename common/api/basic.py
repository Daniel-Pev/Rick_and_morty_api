"""
Basic class for API
"""
import requests

from common.helper.logger import log
import allure



class Api:
    HEADERS = {'Content-Type': 'application/json'}
    TIMEOUT = 10

    def __init__(self):
        """
        Initialization
        """
        self.response = None
        self.url = 'https://rickandmortyapi.com/api'

    def get(self, url: str, params: dict = None, json_body: dict = None):
        """
        Basic get-request
        """
        with allure.step('sending get request'):
            self.response = requests.get(url=url,
                                         headers=self.HEADERS,
                                         params=params,
                                         json=json_body,
                                         timeout=self.TIMEOUT)
            log(response=self.response, request_body=json_body)
            return self

    def check_status_code(self, expected_code: int):
        with allure.step('checking status code'):
            response_code = self.response.status_code
            assert expected_code == response_code, f"\nОжидаемый результат: {expected_code} " \
                                                   f"\nФактический результат: {response_code}"
            return self
