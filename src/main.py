from .interface.main_window import Ui_MainWindow
from .interface.window_util import set_initial_state
from .data import get_player
from .util import format_date

from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtGui, QtCore

import requests


class Main(Ui_MainWindow):
    """
    Chess-Dot-Py main class
    """

    # Username of the last loaded player
    last_loaded_player = None

    def __init__(self, window):
        """
        Initializes the window
        """
        super().__init__()
        self.player_downloader = PlayerDownloader()
        self.setupUi(window)
        self.set_connections()
        self.set_initial_state()
        window.resize(600, 500)
        window.show()

    def set_connections(self):
        """
        Connects UI elements to functions
        """
        self.pushButtonPlayerSearch.clicked.connect(self.button_search_clicked)
        self.pushButtonPlayerReload.clicked.connect(self.button_reload_clicked)
        self.pushButtonPlayerClear.clicked.connect(self.button_clear_clicked)
        self.player_downloader.downloaded.connect(self.player_data_downloaded)

    def set_initial_state(self):
        """
        Sets initial state for some UI elements
        """
        set_initial_state(self)

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

        player = data["player"]

        if player == None:
            self.set_initial_state()
        else:
            # Total stats
            stats = player.stats
            self.lineEditTotalGames.setText(str(stats.get_total_games()))
            self.lineEditTotalWins.setText(str(stats.get_total_wins()))
            self.lineEditTotalLosses.setText(str(stats.get_total_losses()))
            self.lineEditTotalDraws.setText(str(stats.get_total_draws()))
            self.lineEditTotalWinrate.setText(str(stats.get_total_winrate()))

            # Profile
            profile = player.profile
            self.lineEditFollowers.setText(str(profile.followers))
            self.lineEditTitle.setText(profile.title)
            self.lineEditLastOnline.setText(format_date(profile.last_online))
            self.lineEditJoinedOn.setText(format_date(profile.joined))
            self.lineEditUsername.setText(profile.username)
            self.lineEditName.setText(profile.name)
            self.lineEditStatus.setText(profile.status)

            # Modes
            # # Daily
            has_section = player.stats.has_section("chess_daily")
            self.tabWidgetSubsection.setTabEnabled(0, has_section)
            self.qWidgetDaily.setEnabled(has_section)
            if has_section:
                section = player.stats.get_section("chess_daily")
                self.lineEditDailyRating.setText(section.get_rating_string())
                self.lineEditDailyGames.setText(
                    str(section.get_total_games()))
                self.lineEditDailyWins.setText(str(section.wins))
                self.lineEditDailyLosses.setText(str(section.losses))
                self.lineEditDailyDraws.setText(str(section.draws))
                self.lineEditDailyWinrate.setText(str(section.get_win_rate()))

            # # Rapid
            has_section = player.stats.has_section("chess_rapid")
            self.tabWidgetSubsection.setTabEnabled(1, has_section)
            self.qWidgetRapid.setEnabled(has_section)
            if has_section:
                section = player.stats.get_section("chess_rapid")
                self.lineEditRapidRating.setText(section.get_rating_string())
                self.lineEditRapidGames.setText(
                    str(section.get_total_games()))
                self.lineEditRapidWins.setText(str(section.wins))
                self.lineEditRapidLosses.setText(str(section.losses))
                self.lineEditRapidDraws.setText(str(section.draws))
                self.lineEditRapidWinrate.setText(str(section.get_win_rate()))

            # # Bullet
            has_section = player.stats.has_section("chess_bullet")
            self.tabWidgetSubsection.setTabEnabled(2, has_section)
            self.qWidgetBullet.setEnabled(has_section)
            if has_section:
                section = player.stats.get_section("chess_bullet")
                self.lineEditBulletRating.setText(section.get_rating_string())
                self.lineEditBulletGames.setText(
                    str(section.get_total_games()))
                self.lineEditBulletWins.setText(str(section.wins))
                self.lineEditBulletLosses.setText(str(section.losses))
                self.lineEditBulletDraws.setText(str(section.draws))
                self.lineEditBulletWinrate.setText(str(section.get_win_rate()))

            # # Blitz
            has_section = player.stats.has_section("chess_blitz")
            self.tabWidgetSubsection.setTabEnabled(3, has_section)
            self.qWidgetBlitz.setEnabled(has_section)
            if has_section:
                section = player.stats.get_section("chess_blitz")
                self.lineEditBlitzRating.setText(section.get_rating_string())
                self.lineEditBlitzGames.setText(
                    str(section.get_total_games()))
                self.lineEditBlitzWins.setText(str(section.wins))
                self.lineEditBlitzLosses.setText(str(section.losses))
                self.lineEditBlitzDraws.setText(str(section.draws))
                self.lineEditBlitzWinrate.setText(str(section.get_win_rate()))

            # Icon
            avatar = data["avatar"]

            if avatar != None:
                avatar_image = QImage()
                avatar_image.loadFromData(avatar)
                self.image.setPixmap(QPixmap(avatar_image))
            else:
                self.image.setPixmap(QtGui.QPixmap("res/avatar.png"))

            # Save
            self.last_loaded_player = data["player_name"]


class PlayerDownloader(QtCore.QThread):
    """
    Downloader class to obtain player data while not
    freezing the interface
    """

    downloaded = QtCore.pyqtSignal(object)

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
        self.downloaded.emit(response)
