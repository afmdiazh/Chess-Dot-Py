"""
Big functions to update the main window
"""

from util import format_date, get_resource_path

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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
    self.image.setPixmap(QPixmap(get_resource_path("resources/avatar.png")))


def update_sections(self, data):
    """
    Updates player tab with the data obtained from the
    player downloader thread, the data item contains
    the following fields:
     - player: player item
     - player_name: player name used in the search
     - avatar: downloaded avatar image
    """
    player = data["player"]

    if player == None:
        self.set_initial_state()
    else:
        # Total stats
        stats = player.stats
        self.lineEditTotalGames.setText(str(stats.get_total_games()))
        self.lineEditTotalWins.setText(str(stats.get_total_wins()))
        self.lineEditTotalLosses.setText(str(stats.get_total_losses()))
        self.lineEditTotalDraws.setText(str(stats.get_total_draws()))
        self.lineEditTotalWinrate.setText(str(stats.get_total_winrate()))

        # Profile
        profile = player.profile
        self.lineEditFollowers.setText(str(profile.followers))
        self.lineEditTitle.setText(profile.title)
        self.lineEditLastOnline.setText(format_date(profile.last_online))
        self.lineEditJoinedOn.setText(format_date(profile.joined))
        self.lineEditUsername.setText(profile.username)
        self.lineEditName.setText(profile.name)
        self.lineEditStatus.setText(profile.status)

        # Modes
        # # Daily
        has_section = player.stats.has_section("chess_daily")
        self.tabWidgetSubsection.setTabEnabled(0, has_section)
        self.qWidgetDaily.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_daily")
            self.lineEditDailyRating.setText(section.get_rating_string())
            self.lineEditDailyGames.setText(
                str(section.get_total_games()))
            self.lineEditDailyWins.setText(str(section.wins))
            self.lineEditDailyLosses.setText(str(section.losses))
            self.lineEditDailyDraws.setText(str(section.draws))
            self.lineEditDailyWinrate.setText(str(section.get_win_rate()))

        # # Rapid
        has_section = player.stats.has_section("chess_rapid")
        self.tabWidgetSubsection.setTabEnabled(1, has_section)
        self.qWidgetRapid.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_rapid")
            self.lineEditRapidRating.setText(section.get_rating_string())
            self.lineEditRapidGames.setText(
                str(section.get_total_games()))
            self.lineEditRapidWins.setText(str(section.wins))
            self.lineEditRapidLosses.setText(str(section.losses))
            self.lineEditRapidDraws.setText(str(section.draws))
            self.lineEditRapidWinrate.setText(str(section.get_win_rate()))

        # # Bullet
        has_section = player.stats.has_section("chess_bullet")
        self.tabWidgetSubsection.setTabEnabled(2, has_section)
        self.qWidgetBullet.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_bullet")
            self.lineEditBulletRating.setText(section.get_rating_string())
            self.lineEditBulletGames.setText(
                str(section.get_total_games()))
            self.lineEditBulletWins.setText(str(section.wins))
            self.lineEditBulletLosses.setText(str(section.losses))
            self.lineEditBulletDraws.setText(str(section.draws))
            self.lineEditBulletWinrate.setText(str(section.get_win_rate()))

        # # Blitz
        has_section = player.stats.has_section("chess_blitz")
        self.tabWidgetSubsection.setTabEnabled(3, has_section)
        self.qWidgetBlitz.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_blitz")
            self.lineEditBlitzRating.setText(section.get_rating_string())
            self.lineEditBlitzGames.setText(
                str(section.get_total_games()))
            self.lineEditBlitzWins.setText(str(section.wins))
            self.lineEditBlitzLosses.setText(str(section.losses))
            self.lineEditBlitzDraws.setText(str(section.draws))
            self.lineEditBlitzWinrate.setText(str(section.get_win_rate()))

        # Icon
        avatar = data["avatar"]

        if avatar != None:
            avatar_image = QImage()
            avatar_image.loadFromData(avatar)
            self.image.setPixmap(QPixmap(avatar_image))
        else:
            self.image.setPixmap(
                QPixmap(get_resource_path("resources/avatar.png")))

        # Save
        self.last_loaded_player = data["player_name"]


def insert_tab(tabWidget, section):
    """
    Inserts tab with any given name, containing
    a table widget with a few different placeholder
    texts
    """
    # Get data
    name = section.name
    players = section.player_list

    # Create tab
    tab = QWidget()
    tab.setObjectName(name)

    # Create layout
    layout = QVBoxLayout(tab)
    layout.setObjectName("verticalLayout_" + name)

    # Create table widget
    tableWidget = QTableWidget(tab)
    tableWidget.setObjectName("tableWidget")
    tableWidget.setColumnCount(2)
    tableWidget.setRowCount(len(players))

    # Horizontal
    # # Name
    item = QTableWidgetItem()
    item.setText("Name")
    tableWidget.setHorizontalHeaderItem(0, item)
    # # Score
    item = QTableWidgetItem()
    item.setText("Score")
    tableWidget.setHorizontalHeaderItem(1, item)

    # Vertical
    for player in players:
        # Index
        index = player.rank - 1

        # Name
        item = QTableWidgetItem()
        item.setText(player.username)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        tableWidget.setItem(index, 0, item)

        # Score
        item = QTableWidgetItem()
        item.setText(str(player.score))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        tableWidget.setItem(index, 1, item)

    # Add table to layout
    layout.addWidget(tableWidget)

    # Add tab
    tabWidget.addTab(tab, section.get_formatted_name())

    # Returns the added table
    return tableWidget
