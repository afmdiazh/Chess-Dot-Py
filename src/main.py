from .interface.main_window import Ui_MainWindow
from .data import get_player, get_leaderboard
from PyQt5 import QtGui


class Main(Ui_MainWindow):
    """
    Chess-Dot-Py main class
    """

    def __init__(self, window):
        """
        Initializes the window
        """
        super().__init__()
        self.setupUi(window)
        window.show()
        self.set_connections()

        # self.image.setPixmap(QtGui.QPixmap("../res/avatar.jpg"))

    def set_connections(self):
        """
        Connects UI elements to functions
        """
        self.pushButtonPlayerSearch.clicked.connect(self.button_search_clicked)

    def button_search_clicked(self):
        """
        Executed when pushButtonPlayerSearch is clicked
        """
        button_text = self.lineEditPlayerSearch.text().strip()
        self.update_player_tab(button_text)

    def update_player_tab(self, player_name):
        """
        Updates player tab
        """
        player = get_player(player_name)

        if player:
            # TODO: Avatar
            avatar = player.profile.avatar_url

            # Total stats
            self.lineEditTotalGames.setText(
                str(player.stats.get_total_games()))
            self.lineEditTotalWins.setText(
                str(player.stats.get_total_wins()))
            self.lineEditTotalLosses.setText(
                str(player.stats.get_total_losses()))
            self.lineEditTotalDraws.setText(
                str(player.stats.get_total_draws()))
            self.lineEditTotalWinrate.setText(
                str(player.stats.get_total_winrate()))

            # Profile
            self.lineEditFollowers.setText(
                str(player.profile.followers))
            self.lineEditTitle.setText(
                player.profile.title)
            self.lineEditLastOnline.setText(
                str(player.profile.last_online))
            self.lineEditJoinedOn.setText(
                str(player.profile.joined))
            self.lineEditUsername.setText(
                player.profile.username)
            self.lineEditName.setText(
                player.profile.name)
            self.lineEditStatus.setText(
                player.profile.status)

            # Modes
            # # Daily
            if player.stats.has_section("chess_daily"):
                section = player.stats.get_section("chess_daily")
                self.lineEditDailyRating.setText(section.get_rating_string())
                self.lineEditDailyGames.setText(
                    str(section.get_total_games()))
                self.lineEditDailyWins.setText(str(section.wins))
                self.lineEditDailyLosses.setText(str(section.losses))
                self.lineEditDailyDraws.setText(str(section.draws))
                self.lineEditDailyWinrate.setText(str(section.get_win_rate()))
            # # Daily
            if player.stats.has_section("chess_rapid"):
                section = player.stats.get_section("chess_rapid")
                self.lineEditRapidRating.setText(section.get_rating_string())
                self.lineEditRapidGames.setText(
                    str(section.get_total_games()))
                self.lineEditRapidWins.setText(str(section.wins))
                self.lineEditRapidLosses.setText(str(section.losses))
                self.lineEditRapidDraws.setText(str(section.draws))
                self.lineEditRapidWinrate.setText(str(section.get_win_rate()))
            # # Bullet
            if player.stats.has_section("chess_bullet"):
                section = player.stats.get_section("chess_bullet")
                self.lineEditBulletRating.setText(section.get_rating_string())
                self.lineEditBulletGames.setText(
                    str(section.get_total_games()))
                self.lineEditBulletWins.setText(str(section.wins))
                self.lineEditBulletLosses.setText(str(section.losses))
                self.lineEditBulletDraws.setText(str(section.draws))
                self.lineEditBulletWinrate.setText(str(section.get_win_rate()))
            # # Blitz
            if player.stats.has_section("chess_blitz"):
                section = player.stats.get_section("chess_blitz")
                self.lineEditBlitzRating.setText(section.get_rating_string())
                self.lineEditBlitzGames.setText(
                    str(section.get_total_games()))
                self.lineEditBlitzWins.setText(str(section.wins))
                self.lineEditBlitzLosses.setText(str(section.losses))
                self.lineEditBlitzDraws.setText(str(section.draws))
                self.lineEditBlitzWinrate.setText(str(section.get_win_rate()))
