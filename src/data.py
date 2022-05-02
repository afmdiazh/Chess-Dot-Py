import chessdotcom as c
from .player.player import Player
from .leaderboard.leaderboard import Leaderboard


def get_leaderboards_json():
    """
    Obtain leaderboards as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_leaderboards().json
    except:
        return None


def get_player_profile_json(username):
    """
    Obtain player profile as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_profile(username).json
    except:
        return None


def get_player_stats_json(username):
    """
    Obtain player stats as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_stats(username).json
    except:
        return None


def get_player_online_status_json(username):
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
    profile = get_player_profile_json(username)
    stats = get_player_stats_json(username)
    if (profile and stats):
        return Player(profile, stats)
    else:
        return None


def get_leaderboard():
    """
    Generates a leaderboard object
    Returns none if the data couldn't be generated
    """
    json_data = get_leaderboards_json()
    if (json_data):
        return Leaderboard(json_data)
    else:
        return None
