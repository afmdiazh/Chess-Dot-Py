import chessdotcom as c
from player import player


def get_leaderboards():
    """
    Obtain leaderboards as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_leaderboards().json
    except:
        return None


def get_player_profile(username):
    """
    Obtain player profile as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_profile(username).json
    except:
        return None


def get_player_stats(username):
    """
    Obtain player stats as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_stats(username).json
    except:
        return None


def is_player_online(username):
    """
    Obtains player's online status as a boolean
    Returns none if it fails to get the data
    """
    try:
        return c.is_player_online(username)
    except:
        return None


def get_player(username):
    """
    Generates a player object containing the profile data and stats
    Returns none if the data couldn't be gathered
    """
    profile = get_player_profile(username)
    stats = get_player_stats(username)
    if (profile and stats):
        return player.Player(profile, stats)
    else:
        return None
