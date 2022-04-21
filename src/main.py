from .interface.main_window import Ui_MainWindow
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
            player.print_basic_info()
