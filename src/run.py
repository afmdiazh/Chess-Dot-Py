from PyQt5 import QtWidgets
from window import Window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    interface = Window(window)
    sys.exit(app.exec_())
