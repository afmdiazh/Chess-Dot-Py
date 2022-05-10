import threading
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QImage, QMovie, QPixmap
from PyQt5.QtWidgets import QLineEdit
from detail_window import DetailWindow

import interface.manager as m
from downloader import (HistoryDownloader, LeaderboardDownloader,
                        PlayerDownloader, PuzzleDownloader)
from history.history import History
from interface.main_window import Ui_MainWindow
from util import get_resource_path, read_field


class Window(QObject, Ui_MainWindow):
    """
    Chess-Dot-Py main window
    """

    # Username of the last loaded player
    last_loaded_player = None

    # Username of the last loaded history
    last_loaded_history = None

    # Last image downloader thread
    last_image_downloader_thread = None

    # URL of the latest puzzle
    puzzle_url = None

    def __init__(self, window):
        """
        Initializes the window
        """
        super().__init__()
        self.player_downloader = PlayerDownloader()
        self.leaderboard_downloader = LeaderboardDownloader()
        self.puzzle_downloader = PuzzleDownloader()
        self.history_downloader = HistoryDownloader()
        self.image_threads = []
        self.setupUi(window)
        self.load_files()
        self.set_connections()
        self.set_initial_window_state()
        window.setWindowIcon(self.window_icon)
        window.resize(700, 600)
        window.show()

    def set_connections(self):
        """
        Connects UI elements and events to functions
        """
        # Buttons
        # # Player
        self.pushButtonPlayerSearch.clicked.connect(self.button_search_clicked)
        self.pushButtonPlayerReload.clicked.connect(self.button_reload_clicked)
        self.pushButtonPlayerClear.clicked.connect(self.button_clear_clicked)
        # # Leaderboard
        self.pushButtonLBUpdate.clicked.connect(self.button_lb_clicked)
        # # Puzzle
        self.pushButtonRevealSolution.clicked.connect(
            self.button_reveal_clicked)
        self.pushButtonGetDailyPuzzle.clicked.connect(
            lambda: self.button_puzzle_clicked(False))
        self.pushButtonGetRandomPuzzle.clicked.connect(
            lambda: self.button_puzzle_clicked(True))
        # # History
        self.pushButtonHistorySearch.clicked.connect(
            self.button_history_search_clicked)
        self.pushButtonHistoryReload.clicked.connect(
            self.button_history_reload_clicked)
        self.pushButtonHistoryClear.clicked.connect(
            self.button_history_clear_clicked)

        # Clicks
        self.image.mouseDoubleClickEvent = self.avatar_double_clicked
        self.labelPuzzleImage.mouseDoubleClickEvent = self.puzzle_double_clicked
        self.tableWidgetHistory.itemDoubleClicked.connect(self.table_clicked)

        # Key presses
        self.lineEditPlayerSearch.returnPressed.connect(
            self.search_enter_pressed)
        self.lineEditPlayerHistory.returnPressed.connect(
            self.history_enter_pressed)

        # Downloaders
        self.player_downloader.done.connect(self.player_data_downloaded)
        self.leaderboard_downloader.done.connect(self.leaderboard_downloaded)
        self.puzzle_downloader.done.connect(self.puzzle_downloaded)
        self.history_downloader.done.connect(self.history_downloaded)

    def load_files(self):
        """
        Loads files needed for the interface
        """
        # Images
        self.check_mark = QPixmap(get_resource_path("resources/checkmark.png"))
        self.cross_mark = QPixmap(get_resource_path("resources/crossmark.png"))
        self.window_icon = QtGui.QIcon(get_resource_path("resources/icon.png"))
        self.empty_image = QPixmap(get_resource_path("resources/empty.png"))
        self.default_avatar = QPixmap(
            get_resource_path("resources/avatar.png"))
        self.default_avatar_bg = QPixmap(
            get_resource_path("resources/avatar_bg.png"))
        self.default_puzzle = QPixmap(
            get_resource_path("resources/puzzle.png"))

        # GIFs
        self.loading = QMovie(get_resource_path("resources/loading.gif"))
        self.loading.start()

    def set_initial_window_state(self):
        """
        Set initial state for some UI elements
        EXECUTED ONLY ONCE AT THE START
        """
        # Player
        m.set_player_initial_state(self)

        # Leaderboard
        self.loadingLeaderboard.setPixmap(self.empty_image)
        self.loadingLeaderboard.setMaximumSize(QtCore.QSize(0, 0))

        # Puzzle
        self.pushButtonRevealSolution.hide()
        self.loadingPuzzle.setMaximumSize(QtCore.QSize(0, 0))
        self.labelPuzzleImage.setPixmap(self.default_puzzle)

        # History
        m.set_history_initial_state(self)

    def search_enter_pressed(self):
        """
        Executed when enter is pressed inside the search text edit
        Loads the profile data of the inputted text if there's any
        """
        button_text = self.lineEditPlayerSearch.text().strip()
        if button_text != "":
            self.fetch_player_data(button_text)

    def history_enter_pressed(self):
        """
        Executed when enter is pressed inside the history text edit
        Loads the profile data of the inputted text if there's any
        """
        button_text = self.lineEditPlayerHistory.text().strip()
        if button_text != "":
            self.fetch_history_data(button_text)

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
            self.lineEditPlayerSearch.setText(self.last_loaded_player)
            self.fetch_player_data(self.last_loaded_player)

    def button_clear_clicked(self):
        """
        Executed when pushButtonPlayerClear is clicked
        Clears all the profile fields
        """
        self.last_loaded_player = None
        self.lineEditPlayerSearch.setText("")
        m.set_player_initial_state(self)

    def button_lb_clicked(self):
        """
        Executed when pushButtonLBUpdate is clicked
        Updates the leaderboard data
        """
        if not self.last_image_downloader_thread or not self.last_image_downloader_thread.is_alive():
            self.update_loading_icon(self.loadingLeaderboard, True)
            self.leaderboard_downloader.start()

    def button_puzzle_clicked(self, random: bool = False):
        """
        Executed when pushButtonGetDailyPuzzle or pushButtonGetRandomPuzzle
        are clicked. Obtains puzzle data
        """
        # Update loading icon
        self.update_loading_icon(self.loadingPuzzle, True)

        # Hide reveal solution button
        self.pushButtonRevealSolution.hide()

        # Start downloader
        self.puzzle_downloader.set_random(random)
        self.puzzle_downloader.start()

    def button_reveal_clicked(self):
        """
        Executed when pushButtonRevealSolution is clicked
        Reveals the solution of the puzzle
        """
        self.lineEditPuzzleSolution.setEchoMode(QLineEdit.Normal)
        self.pushButtonRevealSolution.hide()

    def button_history_search_clicked(self):
        """
        Executed when pushButtonHistorySearch is clicked
        Loads the profile data of the inputted text if there's any
        """
        button_text = self.lineEditPlayerHistory.text().strip()
        if button_text != "":
            self.fetch_history_data(button_text)

    def button_history_reload_clicked(self):
        """
        Executed when pushButtonHistoryReload is clicked
        Reloads the last searched profile if there's any
        """
        if self.last_loaded_history != None:
            self.lineEditPlayerHistory.setText(self.last_loaded_history)
            self.fetch_history_data(self.last_loaded_history)

    def button_history_clear_clicked(self):
        """
        Executed when pushButtonPlayerClear is clicked
        Clears all the profile fields
        """
        self.last_loaded_history = None
        self.lineEditPlayerHistory.setText("")
        m.set_history_initial_state(self)

    def avatar_double_clicked(self, item: any):
        """
        Executed when a player's avatar is double clicked
        Opens the webbrowser and loads the player's profile
        """
        if self.last_loaded_player != None:
            webbrowser.open("https://www.chess.com/es/member/%s" %
                            self.last_loaded_player)

    def puzzle_double_clicked(self, item: any):
        """
        Executed when the puzzle image is double clicked
        Opens the webbrowser and loads the puzzle tab
        Only daily puzzle can be clicked to open tab
        """
        if self.puzzle_url != None:
            webbrowser.open(self.puzzle_url)

    def fetch_player_data(self, player_name: str):
        """
        Starts the player data download thread with the given
        player name
        """
        self.update_loading_icon(self.loadingPlayer, True)
        self.player_downloader.set_player_name(player_name)
        self.player_downloader.start()

    def fetch_history_data(self, player_name: str):
        """
        Starts the match history download thread with the given
        player name
        """
        self.update_loading_icon(self.loadingHistory, True)
        self.history_downloader.set_player_name(player_name)
        self.history_downloader.start()

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
        # self.update_loading_icon(self.loadingPlayer, False)

    def leaderboard_downloaded(self, leaderboard: object):
        """
        Updates leaderboard tab with the data obtained from the
        leaderboard downloader thread. Adds one tab per section inside
        the leaderboard object.
        """
        # Only executed if downloaded properly
        if not leaderboard:
            self.update_loading_icon(self.loadingLeaderboard, False, True)
            m.show_popup_window(
                "Error", "Couldn't load leaderboard", "Error", window_icon=self.window_icon)
        else:
            # Store index
            last_index = self.tabWidgetLeaderboard.currentIndex()

            # Clear leaderboard widget
            self.tabWidgetLeaderboard.clear()

            # Thread list
            self.image_threads.clear()

            # Add the tabs
            for section in leaderboard.section_list:
                self.image_threads.append(m.insert_lb_tab(
                    self.tabWidgetLeaderboard, section, self))

            # Check if index is in range, for example:
            # Tab amount -> 13, max index -> 12
            if self.tabWidgetLeaderboard.count() > last_index:
                # Set back the index
                self.tabWidgetLeaderboard.setCurrentIndex(last_index)

            # Start the threads
            thread = threading.Thread(
                target=self.start_image_threads, daemon=True, args=())
            thread.start()

            # Save as last
            self.last_image_downloader_thread = thread

    def puzzle_downloaded(self, data):
        """
        Updates puzzle tab with data obtained from the
        puzzle downloader thread
        """
        puzzle = read_field(data, "puzzle")

        # If puzzle doesn't exist
        if puzzle == None:
            # Update loading icon
            self.update_loading_icon(self.loadingPuzzle, False, False, True)
            # Show error
            m.show_popup_window("Error", "Couldn't load puzzle",
                                "Error", window_icon=self.window_icon)
        else:
            # Update loading icon
            self.update_loading_icon(self.loadingPuzzle, False, True)

            # Show reveal solution button
            self.pushButtonRevealSolution.show()

            # Set title and description
            self.lineEditPuzzleTitle.setText(puzzle.get_title())
            self.lineEditPuzzleSolution.setText(puzzle.get_solution())
            self.labelPuzzleExtraData.setText(puzzle.get_extra_data())
            self.lineEditPuzzleSolution.setEchoMode(QLineEdit.Password)

            # Set image
            image = read_field(data, "image")
            if image != None:
                puzzle_image = QImage()
                puzzle_image.loadFromData(image)
                self.labelPuzzleImage.setPixmap(QPixmap(puzzle_image))

            # Set URL
            if puzzle.is_random:
                self.puzzle_url = None
            else:
                self.puzzle_url = puzzle.url

    def history_downloaded(self, history: History):
        """
        Updates history tab with data obtained
        from the history downloader thread
        """
        m.update_history(self, history)

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

    def table_clicked(self, item: object):
        """
        Executed when a table element is clicked
        Shows a menu with different actions
        """

        # Obtain the parent table
        parent_table = item.tableWidget()

        # Obtain row and column for the username
        column = parent_table.usernameIndex()
        row = item.row()

        # Return if column is not set
        if column == -1:
            return

        # Obtain the username item
        username_item = parent_table.item(row, column)

        # Return if item not found
        if username_item == None:
            return

        # Obtain the username text
        username = username_item.text().strip()

        # Create menu
        self.menu = QtWidgets.QMenu(parent_table)
        self.menu.setTitle(username)  # Doesn't work with theme

        # Show username
        show_username = QtWidgets.QAction(username, self)
        self.menu.addAction(show_username)
        self.menu.addSeparator()

        # Go to profile
        go_to_profile = QtWidgets.QAction('Profile', self)
        go_to_profile.triggered.connect(
            lambda: self.go_to_profile(username))
        self.menu.addAction(go_to_profile)

        # Go to history
        go_to_history = QtWidgets.QAction('History', self)
        go_to_history.triggered.connect(
            lambda: self.go_to_history(username))
        self.menu.addAction(go_to_history)

        # Open detail window
        extra_data = parent_table.getEntryData(row)
        print(extra_data)
        if extra_data != None:
            open_detail_window = QtWidgets.QAction('Detail', self)
            open_detail_window.triggered.connect(
                lambda: self.open_detail_window(extra_data))
            self.menu.addAction(open_detail_window)

        # Show menu
        self.menu.popup(QtGui.QCursor.pos())

    def go_to_profile(self, username: str = ""):
        """
        Jumps to a player's profile
        """
        if username != "":
            self.tabWidgetMain.setCurrentIndex(0)
            self.lineEditPlayerSearch.setText(username)
            self.fetch_player_data(username)

    def go_to_history(self, username: str = ""):
        """
        Jumps to a player's history
        """
        if username != "":
            self.tabWidgetMain.setCurrentIndex(3)
            self.lineEditPlayerHistory.setText(username)
            self.fetch_history_data(username)

    def open_detail_window(self, extra_data: object):
        """
        Generates a detail window with the given data
        """
        self.detail_window = DetailWindow(extra_data)

    def update_loading_icon(self, label: object, enabled: bool, clear: bool = False, failed: bool = False):
        """
        Updates loading icon for the given label
        If enabled is true, sets the loading GIF
        If else, sets the checkmark or disables the label
        """
        label.setMaximumSize(QtCore.QSize(20, 20))
        label.show()
        if enabled:
            label.setMovie(self.loading)
            # self.loading.start()
        else:
            # self.loading.stop()
            if clear:
                label.hide()
                label.setPixmap(self.empty_image)
                label.setMaximumSize(QtCore.QSize(0, 0))
            else:
                if failed:
                    label.setPixmap(self.cross_mark)
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
