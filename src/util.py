"""
Utility functions
"""


import datetime


def read_field(json, field):
    """
    Reads a field from a json object
    If the field doesn't exist, returns None
    """
    if field in json:
        return json[field]
    else:
        return None


def format_date(ms):
    """
    Converts date format from miliseconds
    to a readable string
    """
    date = datetime.datetime.fromtimestamp(ms)
    return date.strftime("%m/%d/%Y, %H:%M:%S")
