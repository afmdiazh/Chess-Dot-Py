import sys

from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

from util import get_resource_path
from window import Window


if __name__ == "__main__":
    # Create app
    app = QtWidgets.QApplication(sys.argv)

    # Extra properties for theme
    extra = {
        'density_scale': '-1',
    }

    # Apply theme
    theme_path = get_resource_path("resources/theme.xml")
    apply_stylesheet(app, theme=theme_path, extra=extra)

    # Create window
    window = QtWidgets.QMainWindow()
    interface = Window(window)
    sys.exit(app.exec_())
