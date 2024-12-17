"""
Character endpoint
"""
import allure

from common.api.basic import Api


class CharacterParams:
    VALID_PARAMS = {
        'name': 'rick',
        'status': 'alive',
        'gender': 'male'
    }


class CharacterApi(Api):
    """
    Methods for characters
    """

    def get_character(self, character_id=None, params=None):
        """
        Get character
        """
        with allure.step('get character by id'):
            if character_id:
                return self.get(url=f'{self.url}/character/{character_id}')
        with allure.step('get character by params'):
            return self.get(url=f'{self.url}/character', params=params)
