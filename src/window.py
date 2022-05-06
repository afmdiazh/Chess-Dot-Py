import threading
import webbrowser

import requests
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QMovie, QPixmap

import interface.manager as m
from const import default_avatar_url
from data import get_leaderboard, get_player
from interface.main_window import Ui_MainWindow
from util import get_resource_path


class Window(Ui_MainWindow):
    """
    Chess-Dot-Py main window
    """

    # Username of the last loaded player
    last_loaded_player = None

    # Last image downloader thread
    last_image_downloader_thread = None

    # Username index in leaderboard
    username_item_column_index = -1

    def __init__(self, window):
        """
        Initializes the window
        """
        super().__init__()
        self.player_downloader = PlayerDownloader()
        self.leaderboard_downloader = LeaderboardDownloader()
        self.image_threads = []
        self.setupUi(window)
        self.load_files()
        self.set_connections()
        self.set_initial_state()
        window.setWindowIcon(self.window_icon)
        window.resize(700, 600)
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

        # Clicks
        self.image.mouseDoubleClickEvent = self.avatar_double_clicked

        # Key presses
        self.lineEditPlayerSearch.returnPressed.connect(
            self.search_enter_pressed)

        # Downloaders
        self.player_downloader.done.connect(self.player_data_downloaded)
        self.leaderboard_downloader.done.connect(self.leaderboard_downloaded)

        # Table (not a connection, assigned in manager)
        self.table_double_clicked_event = self.table_double_clicked

    def load_files(self):
        """
        Loads files needed for the interface
        """
        # Images
        self.check_mark = QPixmap(get_resource_path("resources/checkmark.png"))
        self.window_icon = QtGui.QIcon(get_resource_path("resources/icon.png"))
        self.empty_image = QPixmap(get_resource_path("resources/empty.png"))
        self.default_avatar = QPixmap(
            get_resource_path("resources/avatar.png"))
        self.default_avatar_bg = QPixmap(
            get_resource_path("resources/avatar_bg.png"))

        # GIFs
        self.loading = QMovie(get_resource_path("resources/loading.gif"))
        self.loading.start()

    def set_initial_state(self):
        """
        Sets initial state for some UI elements
        """
        m.set_initial_state(self)
        self.loadingLeaderboard.setPixmap(self.empty_image)
        self.loadingLeaderboard.setMaximumSize(QtCore.QSize(0, 0))

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

    def avatar_double_clicked(self, item):
        """
        Executed when a player's avatar is double clicked
        Opens the webbrowser and loads the player's profile
        """
        if self.last_loaded_player != None:
            webbrowser.open("https://www.chess.com/es/member/%s" %
                            self.last_loaded_player)

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
        if not self.last_image_downloader_thread or not self.last_image_downloader_thread.is_alive():
            self.update_loading_icon(self.loadingLeaderboard, True)
            self.leaderboard_downloader.start()

    def fetch_player_data(self, player_name: str):
        """
        Starts the player data download thread with the given
        player name
        """
        self.update_loading_icon(self.loadingPlayer, True)
        self.player_downloader.set_player_name(player_name)
        self.player_downloader.start()

    def player_data_downloaded(self, data: dict):
        """
        Updates player tab with the data obtained from the
        player downloader thread, the data item contains
        the following fields:
         - player: player item
         - player_name: player name used in the search
         - avatar: downloaded avatar image
        """
        m.update_sections(self, data)
        self.update_loading_icon(self.loadingPlayer, False)

    def leaderboard_downloaded(self, leaderboard: object):
        """
        Updates leaderboard tab with the data obtained from the
        leaderboard downloader thread. Adds one tab per section inside
        the leaderboard object.
        """
        # Only executed if downloaded properly
        if not leaderboard:
            m.show_popup_window("Error", "Couldn't load leaderboard", "Error")
        else:
            # Clear leaderboard widget
            self.tabWidgetLeaderboard.clear()

            # Thread list
            self.image_threads.clear()

            # Add the tabs
            for section in leaderboard.section_list:
                self.image_threads.append(m.insert_lb_tab(
                    self.tabWidgetLeaderboard, section, self))

            # Start the threads
            thread = threading.Thread(
                target=self.start_image_threads, daemon=True, args=())
            thread.start()

            # Save as last
            self.last_image_downloader_thread = thread

    def start_image_threads(self):
        """
        Executes all the image downloading threads at once
        Joins them so when they all end the loading icon stops
        """
        # Start the threads to update images
        for thread in self.image_threads:
            thread.start()

        # Join threads
        for thread in self.image_threads:
            thread.join()

        # Update loading icon when the threads are finished
        self.update_loading_icon(self.loadingLeaderboard, False, True)

        # Remove all threads
        self.image_threads.clear()

    def table_double_clicked(self, item: object):
        """
        Executed when a leaderboard table element is double clicked
        Redirects to the player tab and loads the profile of the clicked player
        """
        if item.column() == self.username_item_column_index:
            username = item.text().strip()
            if username != "":
                self.tabWidgetMain.setCurrentIndex(0)
                self.lineEditPlayerSearch.setText(username)
                self.fetch_player_data(username)

    def update_loading_icon(self, label: object, enabled: bool, clear: bool = False):
        """
        Updates loading icon for the given label
        If enabled is true, sets the loading GIF
        If else, sets the checkmark or disables the label
        """
        label.setMaximumSize(QtCore.QSize(20, 20))
        if enabled:
            label.setMovie(self.loading)
            # self.loading.start()
        else:
            # self.loading.stop()
            if clear:
                label.setPixmap(self.empty_image)
                label.setMaximumSize(QtCore.QSize(0, 0))
            else:
                label.setPixmap(self.check_mark)

    def find_first_subsection_tab(self):
        """
        Finds the first enable tab inside the subsection widget
        """
        for i in range(5):
            if self.tabWidgetSubsection.isTabVisible(i):
                return i
        return 0


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
