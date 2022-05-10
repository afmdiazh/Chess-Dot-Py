from PyQt5.QtWidgets import QMainWindow
from history.history import Game
from interface.detail_window import Ui_MainWindow
from leaderboard.leaderboard import LPlayer
from const import detail_game, detail_player


class DetailWindow(QMainWindow, Ui_MainWindow):
    """
    Chess-Dot-Py detail window
    """

    def __init__(self, data: object, icon: object):
        """
        Initializes the window
        """
        super().__init__()
        if data != None:
            self.window = QMainWindow()

            # Add interface elements
            self.setupUi(self.window)

            # Set window title and icon
            self.window.setWindowTitle("Detail")
            self.window.setWindowIcon(icon)

            # Try to process data, exit if it crashes
            self.data = data
            try:
                self.process_data()
            except:
                return

            # Only show after data has been processed
            self.window.show()

    def process_data(self):
        """
        Calls data processing function based on type
        """
        if type(self.data) == Game:
            self.process_game()
        elif type(self.data) == LPlayer:
            self.process_leaderboard_player()

    def process_game(self):
        """
        Processes detailed game data
        """
        game = self.data
        text = detail_game % (
            game.time_control,
            game.get_date(),
            game.rated,
            game.uuid,
            game.time_class,
            game.rules,
            game.white.username,
            game.white.rating,
            game.white.result,
            game.white.id,
            game.white.uuid,
            game.white.accuracy,
            game.black.username,
            game.black.rating,
            game.black.result,
            game.black.id,
            game.black.uuid,
            game.black.accuracy
        )
        self.label.setText(text)

    def process_leaderboard_player(self):
        """
        Processes detailed player data
        """
        player = self.data
        text = detail_player % (
            player.player_id,
            player.api_id,
            player.username,
            player.score,
            player.rank,
            player.get_country(),
            player.status,
            player.avatar_url,
            player.get_flair(),
            player.name,
            player.wins,
            player.losses,
            player.draws,
            player.get_winrate()
        )
        self.label.setText(text)
