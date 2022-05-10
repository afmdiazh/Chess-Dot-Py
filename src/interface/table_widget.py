from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget


class TableWidget(QTableWidget):
    """
    Table subclass for ChessDotPy
    """

    table_type = None
    user_name_index = -1

    def __init__(self, *args, **kwargs):
        QTableWidget.__init__(self)

    def setTableType(self, type: str):
        """
        Sets the table type:
         - "history"
         - "leaderboard"
        """
        self.table_type = type

    def setUsernameIndex(self, index: int):
        """
        Sets the index for the username
        """
        self.user_name_index = index

    def usernameIndex(self):
        """
        Obtains username index
        """
        return self.user_name_index

    def tableType(self):
        """
        Obtains current table type
        """
        return self.table_type
