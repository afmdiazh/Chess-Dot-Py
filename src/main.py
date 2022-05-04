import sys
from window import Window
from PyQt5 import QtWidgets
from util import get_resource_path
from qt_material import apply_stylesheet

if __name__ == "__main__":
    # Create app
    app = QtWidgets.QApplication(sys.argv)

    # Extra properties for theme
    extra = {
        'density_scale': '-1',
    }

    # Apply theme
    theme_path = get_resource_path("resources/dark_amber.xml")
    apply_stylesheet(app, theme=theme_path, extra=extra)

    # Create window
    window = QtWidgets.QMainWindow()
    interface = Window(window)
    sys.exit(app.exec_())
