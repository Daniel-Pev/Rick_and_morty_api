"""
Character endpoint
"""

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
        if character_id:
            return self.get(url=f'{self.url}/character/{character_id}')
        else:
            return self.get(url=f'{self.url}/character', params=params)


char = CharacterApi()
char.get_character(character_id=None)
