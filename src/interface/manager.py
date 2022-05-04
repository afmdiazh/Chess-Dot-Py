"""
Big functions to update the main window
"""

import threading
import requests
from util import format_date

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def set_initial_state(self):
    """
    Sets initial state for some UI elements
    """
    # Subsections
    for index in range(4):
        self.tabWidgetSubsection.setTabEnabled(index, False)
        self.tabWidgetSubsection.setTabVisible(index, False)

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
    self.image.setPixmap(self.default_avatar)

    # Loading icon
    self.loadingPlayer.setPixmap(self.empty_image)
    self.loadingPlayer.setMaximumSize(QtCore.QSize(0, 0))


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
        self.lineEditTotalWinrate.setText(stats.get_total_winrate())

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
        self.tabWidgetSubsection.setTabVisible(0, has_section)
        self.qWidgetDaily.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_daily")
            self.lineEditDailyRating.setText(section.get_rating_string())
            self.lineEditDailyGames.setText(
                str(section.get_total_games()))
            self.lineEditDailyWins.setText(str(section.wins))
            self.lineEditDailyLosses.setText(str(section.losses))
            self.lineEditDailyDraws.setText(str(section.draws))
            self.lineEditDailyWinrate.setText(section.get_win_rate())

        # # Rapid
        has_section = player.stats.has_section("chess_rapid")
        self.tabWidgetSubsection.setTabEnabled(1, has_section)
        self.tabWidgetSubsection.setTabVisible(1, has_section)
        self.qWidgetRapid.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_rapid")
            self.lineEditRapidRating.setText(section.get_rating_string())
            self.lineEditRapidGames.setText(
                str(section.get_total_games()))
            self.lineEditRapidWins.setText(str(section.wins))
            self.lineEditRapidLosses.setText(str(section.losses))
            self.lineEditRapidDraws.setText(str(section.draws))
            self.lineEditRapidWinrate.setText(section.get_win_rate())

        # # Bullet
        has_section = player.stats.has_section("chess_bullet")
        self.tabWidgetSubsection.setTabEnabled(2, has_section)
        self.tabWidgetSubsection.setTabVisible(2, has_section)
        self.qWidgetBullet.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_bullet")
            self.lineEditBulletRating.setText(section.get_rating_string())
            self.lineEditBulletGames.setText(
                str(section.get_total_games()))
            self.lineEditBulletWins.setText(str(section.wins))
            self.lineEditBulletLosses.setText(str(section.losses))
            self.lineEditBulletDraws.setText(str(section.draws))
            self.lineEditBulletWinrate.setText(section.get_win_rate())

        # # Blitz
        has_section = player.stats.has_section("chess_blitz")
        self.tabWidgetSubsection.setTabEnabled(3, has_section)
        self.tabWidgetSubsection.setTabVisible(3, has_section)
        self.qWidgetBlitz.setEnabled(has_section)
        if has_section:
            section = player.stats.get_section("chess_blitz")
            self.lineEditBlitzRating.setText(section.get_rating_string())
            self.lineEditBlitzGames.setText(
                str(section.get_total_games()))
            self.lineEditBlitzWins.setText(str(section.wins))
            self.lineEditBlitzLosses.setText(str(section.losses))
            self.lineEditBlitzDraws.setText(str(section.draws))
            self.lineEditBlitzWinrate.setText(section.get_win_rate())

        # Icon
        avatar = data["avatar"]

        if avatar != None:
            avatar_image = QImage()
            avatar_image.loadFromData(avatar)
            self.image.setPixmap(QPixmap(avatar_image))
        else:
            self.image.setPixmap(self.default_avatar)

        # Save
        self.last_loaded_player = data["player_name"]


def insert_lb_tab(tabWidget, section, self):
    """
    Inserts a tab to a tabWidget loading data from a section
    The tab contains a table with player data from the section object
    Table is returned so it can be linked to events
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
    tableWidget.setRowCount(len(players))

    # Horizontal
    fields = [
        "Username",
        "Name",
        "Score",
        "Stats",
        "Country",
        "Flair",
        "Image"
    ]

    # Column amount
    tableWidget.setColumnCount(len(fields))

    # Add all the fields
    for field in fields:
        item = QTableWidgetItem()
        item.setText(field)
        tableWidget.setHorizontalHeaderItem(fields.index(field), item)

    # Label list for images
    image_label_list = []

    # Vertical
    for player in players:
        # Index / rank of the player
        index = players.index(player)

        # Values to append to the table
        values = [
            player.username,
            player.name,
            str(player.score),
            player.get_formatted_stats(),
            player.get_country(),
            player.get_flair()
        ]

        # Loop trough value list
        for value in values:
            item = QTableWidgetItem()
            item.setText(value)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            tableWidget.setItem(index, values.index(value), item)

        # Profile picture
        label = QtWidgets.QLabel("")
        label.setMaximumSize(QtCore.QSize(20, 20))
        label.setScaledContents(True)
        tableWidget.setCellWidget(index, fields.index("Image"), label)
        image_label_list.append(label)

    # Update images on thread
    thread = threading.Thread(target=download_images, args=(image_label_list, players,))
    thread.start()

    # Resize columns
    header = tableWidget.horizontalHeader()
    for i in range(len(fields)):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # Add table to layout
    layout.addWidget(tableWidget)

    # Add tab
    tabWidget.addTab(tab, section.get_formatted_name())

    # Add event
    tableWidget.itemDoubleClicked.connect(self.table_double_clicked_event)

def download_images(labels, players):
    """
    Downloads player image and assigns it to a label
    """
    for player in players:
        # Download image
        image = requests.get(player.avatar_url).content
        avatar_image = QImage()
        avatar_image.loadFromData(image)
        avatar_pixmap = QPixmap(avatar_image)
        # Assign pixmap to label by index
        index = players.index(player)
        labels[index].setPixmap(avatar_pixmap)
