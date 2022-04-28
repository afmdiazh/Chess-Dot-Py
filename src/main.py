from .interface.main_window import Ui_MainWindow
from .interface.window_util import set_initial_state
from .data import get_player, get_leaderboard


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
        self.set_initial_state()

    def set_connections(self):
        """
        Connects UI elements to functions
        """
        self.pushButtonPlayerSearch.clicked.connect(self.button_search_clicked)

    def set_initial_state(self):
        """
        Sets initial state for some UI elements
        """
        set_initial_state(self)

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

        if player == None:
            self.set_initial_state()
        else:
            # TODO: Avatar
            avatar = player.profile.avatar_url

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
            self.lineEditLastOnline.setText(str(profile.last_online))
            self.lineEditJoinedOn.setText(str(profile.joined))
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
