"""
Utility functions for window
"""


def set_initial_state(self):
    """
    Sets initial state for some UI elements
    """
    for index in range(4):
        self.tabWidgetSubsection.setTabEnabled(index, False)
    self.tabWidgetSubsection.setCurrentIndex(0)
    self.qWidgetBlitz.setEnabled(False)
    self.qWidgetBullet.setEnabled(False)
    self.qWidgetRapid.setEnabled(False)
    self.qWidgetDaily.setEnabled(False)

    self.lineEditTotalGames.setText("")
    self.lineEditTotalWins.setText("")
    self.lineEditTotalLosses.setText("")
    self.lineEditTotalDraws.setText("")
    self.lineEditTotalWinrate.setText("")

    self.lineEditFollowers.setText("")
    self.lineEditTitle.setText("")
    self.lineEditLastOnline.setText("")
    self.lineEditJoinedOn.setText("")
    self.lineEditUsername.setText("")
    self.lineEditName.setText("")
    self.lineEditStatus.setText("")

    self.lineEditDailyRating.setText("")
    self.lineEditDailyGames.setText("")
    self.lineEditDailyWins.setText("")
    self.lineEditDailyLosses.setText("")
    self.lineEditDailyDraws.setText("")
    self.lineEditDailyWinrate.setText("")

    self.lineEditRapidRating.setText("")
    self.lineEditRapidGames.setText("")
    self.lineEditRapidWins.setText("")
    self.lineEditRapidLosses.setText("")
    self.lineEditRapidDraws.setText("")
    self.lineEditRapidWinrate.setText("")

    self.lineEditBulletRating.setText("")
    self.lineEditBulletGames.setText("")
    self.lineEditBulletWins.setText("")
    self.lineEditBulletLosses.setText("")
    self.lineEditBulletDraws.setText("")
    self.lineEditBulletWinrate.setText("")

    self.lineEditBlitzRating.setText("")
    self.lineEditBlitzGames.setText("")
    self.lineEditBlitzWins.setText("")
    self.lineEditBlitzLosses.setText("")
    self.lineEditBlitzDraws.setText("")
    self.lineEditBlitzWinrate.setText("")
