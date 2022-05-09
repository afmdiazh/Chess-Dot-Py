from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class ImageWidget(QLabel):
    """
    QLabel subclass, designed to keep the aspect ratio
    of the image it contains
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self)

    def resizeEvent(self, event=None):
        """
        Change the pixmap size on resize event to
        keep the image's aspect ratio
        """
        if self._pixmap != None and not self._pixmap.isNull():
            pixmap = QPixmap(self._pixmap)
            self.setPixmapInternal(pixmap.scaled(
                self.width(), self.height(), QtCore.Qt.KeepAspectRatio))

    def setPixmap(self, a0: QPixmap) -> None:
        """
        Overwritten setPixmap function to store the added pixmap
        Original pixmap is stores dince it will be overwritten by
        the resize event pixmap scaling
        """
        self._pixmap = a0
        self.resizeEvent()
        return super().setPixmap(a0)

    def setPixmapInternal(self, a0: QPixmap) -> None:
        """
        Set the pixmap without overwriting the _pixmap property
        """
        return super().setPixmap(a0)
