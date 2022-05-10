import requests
from PyQt5 import QtCore

from const import default_avatar_url
from data import get_history, get_leaderboard, get_player, get_puzzle


class PlayerDownloader(QtCore.QThread):
    """
    Downloader class to obtain player data while not
    freezing the interface
    """

    done = QtCore.pyqtSignal(object)
    default_profile_picture = None

    def __init__(self):
        """
        Constructor
        """
        QtCore.QThread.__init__(self)

    def set_player_name(self, player_name: str):
        """
        Updates player name for download
        """
        self.player_name = player_name

    def run(self):
        """
        Obtains the player data and emits response
        """
        # Base response
        response = {
            "player_name": self.player_name,
            "player": None,
            "avatar": None
        }

        # Obtains player
        player = get_player(self.player_name)
        response["player"] = player

        # If player exists
        if player:

            # Downloading avatar if it exists
            avatar_url = player.profile.avatar_url
            if avatar_url != None:
                if avatar_url == default_avatar_url:
                    response["avatar"] = None
                else:
                    try:
                        response["avatar"] = requests.get(avatar_url).content
                    except:
                        response["avatar"] = None

        # Emits response
        self.done.emit(response)


class LeaderboardDownloader(QtCore.QThread):
    """
    Downloader class to obtain leaderboard data
    """

    done = QtCore.pyqtSignal(object)

    def __init__(self):
        """
        Constructor
        """
        QtCore.QThread.__init__(self)

    def run(self):
        """
        Obtains the leaderboard data and emits response
        """
        leaderboard = get_leaderboard()
        self.done.emit(leaderboard)


class PuzzleDownloader(QtCore.QThread):
    """
    Downloader class to obtain puzzle data
    """

    done = QtCore.pyqtSignal(object)

    def __init__(self):
        """
        Constructor
        """
        QtCore.QThread.__init__(self)

    def set_random(self, random: bool):
        """
        Updates the random attribute
        """
        self.random = random

    def run(self):
        """
        Obtains the puzzle data and emits response
        """
        # Get puzzle
        puzzle = get_puzzle(self.random)

        # Base response
        response = {
            "puzzle": puzzle,
            "image": None
        }

        # If puzzle exists
        if puzzle:
            # Downloading image if it exists
            url = puzzle.image_url
            if url != None:
                try:
                    response["image"] = requests.get(url).content
                except:
                    response["image"] = None

        self.done.emit(response)


class HistoryDownloader(QtCore.QThread):
    """
    Downloader class to obtain history data
    """

    done = QtCore.pyqtSignal(object)

    def __init__(self):
        """
        Constructor
        """
        QtCore.QThread.__init__(self)

    def set_player_name(self, player_name: str):
        """
        Updates player name for download
        """
        self.player_name = player_name

    def run(self):
        """
        Obtains the history data and emits response
        """
        history = get_history(self.player_name)
        self.done.emit(history)
