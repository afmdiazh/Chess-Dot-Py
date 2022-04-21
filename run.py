from PyQt5 import QtWidgets
from src.main import Main

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Main(window)
    sys.exit(app.exec_())
