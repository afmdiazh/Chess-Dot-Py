"""
Big functions to update the main window
"""

import threading

import requests
from const import default_avatar_url
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from util import format_date


def set_initial_state(self: object):
    """
    Sets initial state for some UI elements
    """
    # Subsections
    for index in range(4):
        self.tabWidgetSubsection.setTabEnabled(index, False)
        self.tabWidgetSubsection.setTabVisible(index, False)

    # Last
    self.tabWidgetSubsection.setTabEnabled(4, True)
    self.tabWidgetSubsection.setTabVisible(4, True)

    # Disable
    self.qWidgetBlitz.setEnabled(False)
    self.qWidgetBullet.setEnabled(False)
    self.qWidgetRapid.setEnabled(False)
    self.qWidgetDaily.setEnabled(False)

    # Change index
    self.tabWidgetSubsection.setCurrentIndex(self.find_first_subsection_tab())

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


def update_sections(self: object, data: dict):
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
        show_popup_window("Error", "Couldn't load player", "Error")
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
        has_at_least_one = False
        current_tab = self.tabWidgetSubsection.currentIndex()

        # # Daily
        has_section = player.stats.has_section("chess_daily")
        self.tabWidgetSubsection.setTabEnabled(0, has_section)
        self.tabWidgetSubsection.setTabVisible(0, has_section)
        self.qWidgetDaily.setEnabled(has_section)
        if has_section:
            has_at_least_one = True
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
            has_at_least_one = True
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
            has_at_least_one = True
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
            has_at_least_one = True
            section = player.stats.get_section("chess_blitz")
            self.lineEditBlitzRating.setText(section.get_rating_string())
            self.lineEditBlitzGames.setText(
                str(section.get_total_games()))
            self.lineEditBlitzWins.setText(str(section.wins))
            self.lineEditBlitzLosses.setText(str(section.losses))
            self.lineEditBlitzDraws.setText(str(section.draws))
            self.lineEditBlitzWinrate.setText(section.get_win_rate())

        # # If no sections
        self.tabWidgetSubsection.setTabEnabled(4, not has_at_least_one)
        self.tabWidgetSubsection.setTabVisible(4, not has_at_least_one)

        # # Change if needed
        if not self.tabWidgetSubsection.isTabVisible(current_tab):
            self.tabWidgetSubsection.setCurrentIndex(
                self.find_first_subsection_tab())

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


def insert_lb_tab(tabWidget: object, section: object, self: object):
    """
    Inserts a tab to a tabWidget loading data from a section
    The tab contains a table with player data from the section object
    Thread is returned so it can be executed to download the profile pictures
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
    tableWidget.setSortingEnabled(True)
    tableWidget.horizontalHeader().setSectionsClickable(True)
    tableWidget.verticalHeader().setVisible(False)
    tableWidget.setRowCount(len(players))

    # Horizontal
    fields = [
        "Rank",
        "Image",
        "Username",
        "Name",
        "Score",
        "Stats",
        "Country",
        "Flair"
    ]

    # Column amount
    tableWidget.setColumnCount(len(fields))

    # Image index
    image_index = fields.index("Image")

    # Username index for clicking event
    self.username_item_column_index = fields.index("Username")

    # Add all the fields
    for field in fields:
        item = QTableWidgetItem()
        item.setText(field)
        tableWidget.setHorizontalHeaderItem(fields.index(field), item)

    # Label list for images
    image_label_list = []
    image_url_list = []

    # Vertical
    for player in players:
        # Index / rank of the player
        index = players.index(player)

        # Values to append to the table
        values = [
            index + 1,
            player.username,
            player.name,
            player.score,
            player.get_formatted_stats(),
            player.get_country(),
            player.get_flair()
        ]

        # Loop trough value list
        for value in values:
            value_index = values.index(value)
            if value_index >= image_index:
                value_index += 1
            item = QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, value)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            tableWidget.setItem(index, value_index, item)

        # Profile picture
        # # Create a frame to hold the layout
        img_frame = QtWidgets.QWidget()

        # # Create a layout to hold the label
        img_layout = QtWidgets.QGridLayout()
        img_layout.setContentsMargins(0, 0, 0, 0)

        # # Create a label to hold the image
        label = QtWidgets.QLabel("")
        label.setMaximumSize(QtCore.QSize(20, 20))
        label.setScaledContents(True)

        # # Set label to layout and djust stretch
        img_layout.addWidget(label, 0, 1)
        img_layout.setColumnStretch(0, 1)
        img_layout.setColumnStretch(2, 1)

        # # Set layout to frame
        img_frame.setLayout(img_layout)

        # # Add frame to the table
        tableWidget.setCellWidget(index, image_index, img_frame)

        # # Add data to lists
        image_label_list.append(label)
        image_url_list.append(player.avatar_url)

    # Update images on thread
    thread = threading.Thread(target=download_images, daemon=True, args=(
        image_label_list, image_url_list, self.default_avatar_bg,))

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

    # Return thread
    return thread


def download_images(labels: list, urls: list, default_image: object):
    """
    Downloads player image and assigns it to a label
    """
    for i in range(len(urls)):
        try:
            if urls[i] == default_avatar_url:
                # If it's default avatar
                labels[i].setPixmap(default_image)
            else:
                # Download image
                image = requests.get(urls[i]).content
                # To Pixmap
                avatar_image = QImage()
                avatar_image.loadFromData(image)
                avatar_pixmap = QPixmap(avatar_image)
                # Set
                labels[i].setPixmap(avatar_pixmap)
        except:
            pass


def show_popup_window(text: str = "text", informative_text: str = "informative_text", title: str = "title", icon: any = QMessageBox.Critical):
    """
    Generates a pop-up window
    """
    window = QMessageBox()
    window.setIcon(icon)
    window.setText(text)
    window.setInformativeText(informative_text)
    window.setWindowTitle(title)
    window.exec_()


def get_size_policy(mode: any = QtWidgets.QSizePolicy.MinimumExpanding):
    """
    Generates a QSizePolicy object with the given policy type
    """
    size_policy = QtWidgets.QSizePolicy(mode, mode)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    return size_policy
