from interface.main_window import Ui_MainWindow
from util import get_resource_path

from data import get_player, get_leaderboard
from PyQt5 import QtCore, QtGui

import interface.manager as m
import requests


class Window(Ui_MainWindow):
    """
    Chess-Dot-Py main window
    """

    # Username of the last loaded player
    last_loaded_player = None

    def __init__(self, window):
        """
        Initializes the window
        """
        super().__init__()
        self.player_downloader = PlayerDownloader()
        self.leaderboard_downloader = LeaderboardDownloader()
        self.setupUi(window)
        self.set_connections()
        self.set_initial_state()
        window.setWindowIcon(QtGui.QIcon(
            get_resource_path('resources/icon.png')))
        window.resize(600, 500)
        window.show()

    def set_connections(self):
        """
        Connects UI elements and events to functions
        """
        # Buttons
        self.pushButtonPlayerSearch.clicked.connect(self.button_search_clicked)
        self.pushButtonPlayerReload.clicked.connect(self.button_reload_clicked)
        self.pushButtonPlayerClear.clicked.connect(self.button_clear_clicked)
        self.pushButtonLBUpdate.clicked.connect(self.button_lb_clicked)

        # Key presses
        self.lineEditPlayerSearch.returnPressed.connect(self.search_enter_pressed)

        # Downloaders
        self.player_downloader.done.connect(self.player_data_downloaded)
        self.leaderboard_downloader.done.connect(self.leaderboard_downloaded)

        # Table (not a connection, assigned in manager)
        self.table_double_clicked_event = self.table_double_clicked

    def set_initial_state(self):
        """
        Sets initial state for some UI elements
        """
        m.set_initial_state(self)

    def search_enter_pressed(self):
        """
        Executed when enter is pressed inside the search text edit
        Loads the profile data of the inputted text if there's any
        """
        button_text = self.lineEditPlayerSearch.text().strip()
        if button_text != "":
            self.fetch_player_data(button_text)

    def button_search_clicked(self):
        """
        Executed when pushButtonPlayerSearch is clicked
        Loads the profile data of the inputted text if there's any
        """
        button_text = self.lineEditPlayerSearch.text().strip()
        if button_text != "":
            self.fetch_player_data(button_text)

    def button_reload_clicked(self):
        """
        Executed when pushButtonPlayerReload is clicked
        Reloads the last searched profile if there's any
        """
        if self.last_loaded_player != None:
            self.fetch_player_data(self.last_loaded_player)

    def button_clear_clicked(self):
        """
        Executed when pushButtonPlayerClear is clicked
        Clears all the profile fields
        """
        self.last_loaded_player = None
        self.set_initial_state()

    def button_lb_clicked(self):
        """
        Executed when pushButtonLBUpdate is clicked
        Updates the leaderboard data
        """
        self.leaderboard_downloader.start()

    def fetch_player_data(self, player_name):
        """
        Starts the player data download thread with the given
        player name
        """
        self.player_downloader.set_player_name(player_name)
        self.player_downloader.start()

    def player_data_downloaded(self, data):
        """
        Updates player tab with the data obtained from the
        player downloader thread, the data item contains
        the following fields:
         - player: player item
         - player_name: player name used in the search
         - avatar: downloaded avatar image
        """
        m.update_sections(self, data)

    def leaderboard_downloaded(self, leaderboard):
        """
        Updates leaderboard tab with the data obtained from the
        leaderboard downloader thread. Adds one tab per section inside
        the leaderboard object.
        """
        self.tabWidgetLeaderboard.clear()
        for section in leaderboard.section_list:
            table = m.insert_lb_tab(self.tabWidgetLeaderboard, section)
            table.itemDoubleClicked.connect(self.table_double_clicked_event)

    def table_double_clicked(self, item):
        """
        Executed when a leaderboard table element is double clicked
        Redirects to the player tab and loads the profile of the clicked player
        """
        if item.column() == 0:
            print("Correct column")
            username = item.text().strip()
            if username != "":
                print("Proper username")
                self.tabWidgetMain.setCurrentIndex(0)
                self.lineEditPlayerSearch.setText(username)
                self.fetch_player_data(username)


class PlayerDownloader(QtCore.QThread):
    """
    Downloader class to obtain player data while not
    freezing the interface
    """

    done = QtCore.pyqtSignal(object)

    def __init__(self):
        """
        Constructor
        """
        QtCore.QThread.__init__(self)

    def set_player_name(self, player_name):
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
