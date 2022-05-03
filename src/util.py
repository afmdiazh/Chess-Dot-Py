"""
Utility functions
"""

import datetime
import os
import sys


def read_field(json, field, default_value = None):
    """
    Reads a field from a json object
    If the field doesn't exist, returns None
    """
    if field in json:
        return json[field]
    else:
        return default_value


def format_date(ms):
    """
    Converts date format from miliseconds
    to a readable string
    """
    date = datetime.datetime.fromtimestamp(ms)
    return date.strftime("%m/%d/%Y, %H:%M:%S")


def get_resource_path(relative_path):
    """
    Obtains the path of a resource, needed for getting
    files from the compiled executable after pyinstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
