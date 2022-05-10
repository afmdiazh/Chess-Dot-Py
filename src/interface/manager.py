"""
Big functions to update the main window
"""

import threading

import requests
from const import default_avatar_url
from history.history import History
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from util import format_date
from window import Window


def set_player_initial_state(window: Window):
    """
    Sets initial state for some UI elements
    """
    # Subsections
    for index in range(4):
        window.tabWidgetSubsection.setTabEnabled(index, False)
        window.tabWidgetSubsection.setTabVisible(index, False)

    # Last
    window.tabWidgetSubsection.setTabEnabled(4, True)
    window.tabWidgetSubsection.setTabVisible(4, True)

    # Disable
    window.qWidgetBlitz.setEnabled(False)
    window.qWidgetBullet.setEnabled(False)
    window.qWidgetRapid.setEnabled(False)
    window.qWidgetDaily.setEnabled(False)

    # Change index
    window.tabWidgetSubsection.setCurrentIndex(
        window.find_first_subsection_tab())

    # Stats
    window.lineEditTotalGames.setText("")
    window.lineEditTotalWins.setText("")
    window.lineEditTotalLosses.setText("")
    window.lineEditTotalDraws.setText("")
    window.lineEditTotalWinrate.setText("")

    # Profile
    window.lineEditFollowers.setText("")
    window.lineEditTitle.setText("")
    window.lineEditLastOnline.setText("")
    window.lineEditJoinedOn.setText("")
    window.lineEditUsername.setText("")
    window.lineEditName.setText("")
    window.lineEditStatus.setText("")

    # Daily subsection
    window.lineEditDailyRating.setText("")
    window.lineEditDailyGames.setText("")
    window.lineEditDailyWins.setText("")
    window.lineEditDailyLosses.setText("")
    window.lineEditDailyDraws.setText("")
    window.lineEditDailyWinrate.setText("")

    # Rapid subsection
    window.lineEditRapidRating.setText("")
    window.lineEditRapidGames.setText("")
    window.lineEditRapidWins.setText("")
    window.lineEditRapidLosses.setText("")
    window.lineEditRapidDraws.setText("")
    window.lineEditRapidWinrate.setText("")

    # Bullet subsection
    window.lineEditBulletRating.setText("")
    window.lineEditBulletGames.setText("")
    window.lineEditBulletWins.setText("")
    window.lineEditBulletLosses.setText("")
    window.lineEditBulletDraws.setText("")
    window.lineEditBulletWinrate.setText("")

    # Blitz subsection
    window.lineEditBlitzRating.setText("")
    window.lineEditBlitzGames.setText("")
    window.lineEditBlitzWins.setText("")
    window.lineEditBlitzLosses.setText("")
    window.lineEditBlitzDraws.setText("")
    window.lineEditBlitzWinrate.setText("")

    # Avatar
    window.image.setText("")
    window.image.setPixmap(window.default_avatar)

    # Loading icon
    window.loadingPlayer.setPixmap(window.empty_image)
    window.loadingPlayer.setMaximumSize(QtCore.QSize(0, 0))


def set_history_initial_state(window: Window, first_execution: bool = True):
    """
    Sets initial state for some UI elements
    """
    # Loading icon
    window.loadingHistory.setPixmap(window.empty_image)
    window.loadingHistory.setMaximumSize(QtCore.QSize(0, 0))

    # Clear table
    window.tableWidgetHistory.setRowCount(0)

    # Only once
    if first_execution:
        # Change column resize mode
        header = window.tableWidgetHistory.horizontalHeader()
        for i in range(window.tableWidgetHistory.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Other (enable sorting, make sections clickable, hide left bar)
        window.tableWidgetHistory.setSortingEnabled(True)
        window.tableWidgetHistory.horizontalHeader().setSectionsClickable(True)
        window.tableWidgetHistory.verticalHeader().setVisible(False)


def update_sections(window: Window, data: dict):
    """
    Updates player tab with the data obtained from the
    player downloader thread, the data item contains
    the following fields:
     - player: player item
     - player_name: player name used in the search
     - avatar: downloaded avatar image
    """
    player = data["player"]

    # If player not found
    if player == None:
        # Reset tab
        set_player_initial_state(window)
        # Update icon to show cross
        window.update_loading_icon(window.loadingPlayer, False, False, True)
        # Show error message
        show_popup_window("Error", "Couldn't load player",
                          "Error", window_icon=window.window_icon)
    else:
        # Total stats
        stats = player.stats
        window.lineEditTotalGames.setText(str(stats.get_total_games()))
        window.lineEditTotalWins.setText(str(stats.get_total_wins()))
        window.lineEditTotalLosses.setText(str(stats.get_total_losses()))
        window.lineEditTotalDraws.setText(str(stats.get_total_draws()))
        window.lineEditTotalWinrate.setText(stats.get_total_winrate())

        # Profile
        profile = player.profile
        window.lineEditFollowers.setText(str(profile.followers))
        window.lineEditTitle.setText(profile.title)
        window.lineEditLastOnline.setText(format_date(profile.last_online))
        window.lineEditJoinedOn.setText(format_date(profile.joined))
        window.lineEditUsername.setText(profile.username)
        window.lineEditName.setText(profile.name)
        window.lineEditStatus.setText(profile.status)

        # Modes
        has_at_least_one = False
        current_tab = window.tabWidgetSubsection.currentIndex()

        # # Daily
        has_section = player.stats.has_section("chess_daily")
        window.tabWidgetSubsection.setTabEnabled(0, has_section)
        window.tabWidgetSubsection.setTabVisible(0, has_section)
        window.qWidgetDaily.setEnabled(has_section)
        if has_section:
            has_at_least_one = True
            section = player.stats.get_section("chess_daily")
            window.lineEditDailyRating.setText(section.get_rating_string())
            window.lineEditDailyGames.setText(
                str(section.get_total_games()))
            window.lineEditDailyWins.setText(str(section.wins))
            window.lineEditDailyLosses.setText(str(section.losses))
            window.lineEditDailyDraws.setText(str(section.draws))
            window.lineEditDailyWinrate.setText(section.get_win_rate())

        # # Rapid
        has_section = player.stats.has_section("chess_rapid")
        window.tabWidgetSubsection.setTabEnabled(1, has_section)
        window.tabWidgetSubsection.setTabVisible(1, has_section)
        window.qWidgetRapid.setEnabled(has_section)
        if has_section:
            has_at_least_one = True
            section = player.stats.get_section("chess_rapid")
            window.lineEditRapidRating.setText(section.get_rating_string())
            window.lineEditRapidGames.setText(
                str(section.get_total_games()))
            window.lineEditRapidWins.setText(str(section.wins))
            window.lineEditRapidLosses.setText(str(section.losses))
            window.lineEditRapidDraws.setText(str(section.draws))
            window.lineEditRapidWinrate.setText(section.get_win_rate())

        # # Bullet
        has_section = player.stats.has_section("chess_bullet")
        window.tabWidgetSubsection.setTabEnabled(2, has_section)
        window.tabWidgetSubsection.setTabVisible(2, has_section)
        window.qWidgetBullet.setEnabled(has_section)
        if has_section:
            has_at_least_one = True
            section = player.stats.get_section("chess_bullet")
            window.lineEditBulletRating.setText(section.get_rating_string())
            window.lineEditBulletGames.setText(
                str(section.get_total_games()))
            window.lineEditBulletWins.setText(str(section.wins))
            window.lineEditBulletLosses.setText(str(section.losses))
            window.lineEditBulletDraws.setText(str(section.draws))
            window.lineEditBulletWinrate.setText(section.get_win_rate())

        # # Blitz
        has_section = player.stats.has_section("chess_blitz")
        window.tabWidgetSubsection.setTabEnabled(3, has_section)
        window.tabWidgetSubsection.setTabVisible(3, has_section)
        window.qWidgetBlitz.setEnabled(has_section)
        if has_section:
            has_at_least_one = True
            section = player.stats.get_section("chess_blitz")
            window.lineEditBlitzRating.setText(section.get_rating_string())
            window.lineEditBlitzGames.setText(
                str(section.get_total_games()))
            window.lineEditBlitzWins.setText(str(section.wins))
            window.lineEditBlitzLosses.setText(str(section.losses))
            window.lineEditBlitzDraws.setText(str(section.draws))
            window.lineEditBlitzWinrate.setText(section.get_win_rate())

        # # If no sections
        window.tabWidgetSubsection.setTabEnabled(4, not has_at_least_one)
        window.tabWidgetSubsection.setTabVisible(4, not has_at_least_one)

        # # Change if needed
        if not window.tabWidgetSubsection.isTabVisible(current_tab):
            window.tabWidgetSubsection.setCurrentIndex(
                window.find_first_subsection_tab())

        # Icon
        avatar = data["avatar"]

        if avatar != None:
            avatar_image = QImage()
            avatar_image.loadFromData(avatar)
            window.image.setPixmap(QPixmap(avatar_image))
        else:
            window.image.setPixmap(window.default_avatar)

        # Save
        window.last_loaded_player = data["player_name"]

        # Icon
        window.update_loading_icon(window.loadingPlayer, False)


def insert_lb_tab(tabWidget: object, section: object, window: Window):
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
    window.username_item_column_index = fields.index("Username")

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
        image_label_list, image_url_list, window.default_avatar_bg,))

    # Resize columns
    header = tableWidget.horizontalHeader()
    for i in range(len(fields)):
        header.setSectionResizeMode(i, QHeaderView.Stretch)

    # Add table to layout
    layout.addWidget(tableWidget)

    # Add tab
    tabWidget.addTab(tab, section.get_formatted_name())

    # Add event
    tableWidget.itemDoubleClicked.connect(window.table_double_clicked_event)

    # Return thread
    return thread


def update_history(window: Window, history: History):
    """
    Updates the history section with the downloaded data
    """
    # If history not found
    if history == None:
        # Reset tab
        set_history_initial_state(window, False)
        # Update icon to show cross
        window.update_loading_icon(window.loadingHistory, False, False, True)
        # Show error message
        show_popup_window("Error", "Couldn't load history",
                          "Error", window_icon=window.window_icon)
    else:
        # Clear table
        window.tableWidgetHistory.setRowCount(0)

        # Game list
        games = history.game_list

        # Reversed because they are in opposite order
        games.reverse()

        # Columns
        column_count = window.tableWidgetHistory.columnCount()

        # Rows
        window.tableWidgetHistory.setRowCount(len(games))

        # Iterate over all the games
        for game in games:
            # Current index
            index = games.index(game)

            # Values
            values = [
                game.opponent_player.username,  # Opponent
                game.get_own_color(),  # Color
                game.get_own_result(),  # Result
                game.get_own_accuracy(),  # Accuracy
                game.get_own_rating(),  # Rating
                game.time_control,  # Format
                game.rules.capitalize(),  # Rules
                game.get_date()  # Date
            ]

            # Adding all the values
            for i in range(len(values)):
                if i < column_count:
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, values[i])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    window.tableWidgetHistory.setItem(index, i, item)

        # Save the last loaded name
        window.last_loaded_history = history.username

        # Change icon
        window.update_loading_icon(window.loadingHistory, False)


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


def show_popup_window(text: str = "text", informative_text: str = "informative_text", title: str = "title", icon: any = QMessageBox.Critical, window_icon: any = None):
    """
    Generates a pop-up window
    """
    window = QMessageBox()
    if window_icon != None:
        window.setWindowIcon(window_icon)
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
