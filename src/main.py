import sys
from PyQt5 import QtWidgets
from window import Window
from qt_material import apply_stylesheet

if __name__ == "__main__":
    # Create app
    app = QtWidgets.QApplication(sys.argv)

    # Extra properties for theme
    extra = {
    'density_scale': '-1',
    }

    # Apply theme
    apply_stylesheet(app, theme='dark_amber.xml', extra=extra)
    
    # Create window
    window = QtWidgets.QMainWindow()
    interface = Window(window)
    sys.exit(app.exec_())
