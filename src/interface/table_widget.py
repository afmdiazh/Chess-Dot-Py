from PyQt5.QtWidgets import QTableWidget

from util import read_field


class TableWidget(QTableWidget):
    """
    Table subclass for ChessDotPy
    """

    table_type = None
    user_name_index = -1
    entry_data = {}
    entry_count = 0

    def __init__(self, *args, **kwargs):
        QTableWidget.__init__(self)

    def setTableType(self, type: str):
        """
        Sets the table type (history, leaderboard)
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

    def clearEntryData(self):
        """
        Clears entry data
        """
        self.entry_data = {}
        self.entry_count = 0

    def addEntryData(self, entry: object, index: int = None):
        """
        Adds a entry to the entry amount
        """
        key = None

        # Get key
        if index == None:
            key = str(self.entry_count)
        else:
            key = str(index)

        # Add and increase count
        self.entry_data[key] = entry
        self.entry_count += 1

    def getEntryData(self, index: int = None):
        """
        Returns the entry data of a given index
        """
        if index == None:
            return self.entry_data
        else:
            return read_field(self.entry_data, str(index))

    def getFormattedData(self, index: int):
        """
        Returns formatted data of a given index
        TODO: Finish
        """
        pass
