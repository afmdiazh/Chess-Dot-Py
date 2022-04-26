"""
Utility class for json objects
"""


def read_field(json, field):
    """
    Reads a field from a json object
    If the field doesn't exist, returns None
    """
    if field in json:
        return json[field]
    else:
        return None
