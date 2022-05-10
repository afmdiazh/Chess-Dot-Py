from PyQt5.QtWidgets import QMainWindow
from interface.detail_window import Ui_MainWindow


class DetailWindow(QMainWindow, Ui_MainWindow):
    """
    Chess-Dot-Py detail window
    """

    def __init__(self, data: object):
        """
        Initializes the window
        """
        super().__init__()
        if data != None:
            self.window = QMainWindow()
            self.setupUi(self.window)
            self.window.show()
