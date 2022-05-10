"""
Utility functions
"""

import datetime
import json
import os
import sys

emojis = None


def read_field(json: dict, field: str, default_value: any = None):
    """
    Reads a field from a json object
    If the field doesn't exist, returns None
    """
    if json == None:
        return default_value
    if field in json:
        return json[field]
    else:
        return default_value


def format_date(ms: int):
    """
    Converts date format from miliseconds
    to a readable string
    """
    try:
        date = datetime.datetime.fromtimestamp(ms)
        return date.strftime("%m/%d/%Y")
    except:
        return "Error parsing date"


def format_date_time(ms: int):
    """
    Converts date format from miliseconds
    to a readable string (more precise)
    """
    try:
        date = datetime.datetime.fromtimestamp(ms)
        return date.strftime("%m/%d/%Y, %H:%M:%S")
    except:
        return "Error parsing date"


def get_resource_path(relative_path: str):
    """
    Obtains the path of a resource, needed for getting
    files from the compiled executable after pyinstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def find_emoji(string: str, default: str = "chess_pawn"):
    """
    Tries to find emoji from Chess.com emoji
    """
    # Directly from json
    if string in emojis:
        return emojis[string]

    # Closest approximation
    names = emojis.keys()
    for name in names:
        if name in string:
            return emojis[name]

    # Not found
    return default


# Load emoji list
try:
    with open(get_resource_path("resources/emoji.json")) as f:
        emojis = json.load(f)
except:
    emojis = {}
