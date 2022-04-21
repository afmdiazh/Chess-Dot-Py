"""
Utility class for json objects
"""


def read_field(json, field):
    if field in json:
        return json[field]
    else:
        return None
