"""
Utility functions for window
"""

from PyQt5 import QtGui, QtCore


def set_initial_state(self):
    """
    Sets initial state for some UI elements
    """
    # Subsections
    for index in range(4):
        self.tabWidgetSubsection.setTabEnabled(index, False)

    self.tabWidgetSubsection.setCurrentIndex(0)
    self.qWidgetBlitz.setEnabled(False)
    self.qWidgetBullet.setEnabled(False)
    self.qWidgetRapid.setEnabled(False)
    self.qWidgetDaily.setEnabled(False)

    # Stats
    self.lineEditTotalGames.setText("")
    self.lineEditTotalWins.setText("")
    self.lineEditTotalLosses.setText("")
    self.lineEditTotalDraws.setText("")
    self.lineEditTotalWinrate.setText("")

    # Profile
    self.lineEditFollowers.setText("")
    self.lineEditTitle.setText("")
    self.lineEditLastOnline.setText("")
    self.lineEditJoinedOn.setText("")
    self.lineEditUsername.setText("")
    self.lineEditName.setText("")
    self.lineEditStatus.setText("")

    # Daily subsection
    self.lineEditDailyRating.setText("")
    self.lineEditDailyGames.setText("")
    self.lineEditDailyWins.setText("")
    self.lineEditDailyLosses.setText("")
    self.lineEditDailyDraws.setText("")
    self.lineEditDailyWinrate.setText("")

    # Rapid subsection
    self.lineEditRapidRating.setText("")
    self.lineEditRapidGames.setText("")
    self.lineEditRapidWins.setText("")
    self.lineEditRapidLosses.setText("")
    self.lineEditRapidDraws.setText("")
    self.lineEditRapidWinrate.setText("")

    # Bullet subsection
    self.lineEditBulletRating.setText("")
    self.lineEditBulletGames.setText("")
    self.lineEditBulletWins.setText("")
    self.lineEditBulletLosses.setText("")
    self.lineEditBulletDraws.setText("")
    self.lineEditBulletWinrate.setText("")

    # Blitz subsection
    self.lineEditBlitzRating.setText("")
    self.lineEditBlitzGames.setText("")
    self.lineEditBlitzWins.setText("")
    self.lineEditBlitzLosses.setText("")
    self.lineEditBlitzDraws.setText("")
    self.lineEditBlitzWinrate.setText("")

    # Avatar
    self.image.setText("")
    self.image.setPixmap(QtGui.QPixmap("res/avatar.png"))
