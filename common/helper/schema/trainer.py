"""
Schema for character
"""
from voluptuous import Schema, PREVENT_EXTRA, ALLOW_EXTRA

valid_character = Schema(
    {
        "id": int,
        "name": str,
        "status": str,
        "species": str,
        "type": str,
        "gender": str,
        "origin": object,
        "location": object,
        "image": str,
        "episode": list,
        "url": str,
        'created': str

    },
    extra=ALLOW_EXTRA,
    required=True

)

error_character = Schema(
    {
        "error": str
    },
    extra=ALLOW_EXTRA,
    required=True
)
