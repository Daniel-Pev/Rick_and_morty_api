"""
Schema for location
"""
from voluptuous import Schema, ALLOW_EXTRA


valid_location = Schema(
    {
        "id": int,
        "name": str,
        "type": str,
        "dimension": str,
        "residents": list,
        "url": str,
        "created": object,
    },
    extra=ALLOW_EXTRA,
    required=True
)
error_location = Schema(
    {
        "error": str
    },
    extra=ALLOW_EXTRA,
    required=True
)
