import datetime
import chessdotcom as c

from leaderboard.leaderboard import Leaderboard
from player.player import Player
from puzzle.puzzle import Puzzle


# User-Agent header
c.Client.config["headers"]["User-Agent"] = (
    "Chess-Dot-Py"
    "https://github.com/mgldz/Chess-Dot-Py"
)


def get_leaderboards_json():
    """
    Obtain leaderboards as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_leaderboards().json
    except:
        return None


def get_player_profile_json(username: str):
    """
    Obtain player profile as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_profile(username).json
    except:
        return None


def get_player_stats_json(username: str):
    """
    Obtain player stats as a json object
    Returns none if it fails to get the data
    """
    try:
        return c.get_player_stats(username).json
    except:
        return None


def get_player_online_status_json(username: str):
    """
    Obtains player's online status as a boolean
    Returns none if it fails to get the data
    """
    try:
        return c.is_player_online(username).json
    except:
        return None


def get_puzzle_json(random: bool = False):
    """
    Obtains daily puzzle
    """
    try:
        if random:
            return c.get_random_daily_puzzle().json
        else:
            return c.get_current_daily_puzzle().json

    except:
        return None


def get_player(username: str):
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


def get_puzzle(random: bool = False):
    """
    Generates a puzzle object
    Returns none if the data couldn't be generated
    """
    json_data = get_puzzle_json(random)
    if (json_data):
        return Puzzle(json_data, random)
    else:
        return None


# Tests
if __name__ == "__main__":
    leaderboard = get_leaderboard()
    magnus = get_player("MagnusCarlsen")
    gotham = get_player("GothamChess")
    hikaru = get_player("Hikaru")
    puzzle = get_puzzle(False)
