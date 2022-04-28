# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutMain = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMain.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayoutMain.setObjectName("horizontalLayoutMain")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.qWidgetPlayer = QtWidgets.QWidget()
        self.qWidgetPlayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.qWidgetPlayer.setObjectName("qWidgetPlayer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.qWidgetPlayer)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditPlayerSearch = QtWidgets.QLineEdit(self.qWidgetPlayer)
        self.lineEditPlayerSearch.setObjectName("lineEditPlayerSearch")
        self.gridLayout_3.addWidget(self.lineEditPlayerSearch, 0, 0, 1, 1)
        self.pushButtonPlayerSearch = QtWidgets.QPushButton(self.qWidgetPlayer)
        self.pushButtonPlayerSearch.setObjectName("pushButtonPlayerSearch")
        self.gridLayout_3.addWidget(self.pushButtonPlayerSearch, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxStats = QtWidgets.QGroupBox(self.qWidgetPlayer)
        self.groupBoxStats.setObjectName("groupBoxStats")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxStats)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayoutStats = QtWidgets.QGridLayout()
        self.gridLayoutStats.setObjectName("gridLayoutStats")
        self.groupBoxTotalStats = QtWidgets.QGroupBox(self.groupBoxStats)
        self.groupBoxTotalStats.setObjectName("groupBoxTotalStats")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxTotalStats)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelGames = QtWidgets.QLabel(self.groupBoxTotalStats)
        self.labelGames.setObjectName("labelGames")
        self.gridLayout_2.addWidget(self.labelGames, 0, 0, 1, 1)
        self.lineEditTotalGames = QtWidgets.QLineEdit(self.groupBoxTotalStats)
        self.lineEditTotalGames.setReadOnly(True)
        self.lineEditTotalGames.setObjectName("lineEditTotalGames")
        self.gridLayout_2.addWidget(self.lineEditTotalGames, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.labelWins = QtWidgets.QLabel(self.groupBoxTotalStats)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelWins.setPalette(palette)
        self.labelWins.setObjectName("labelWins")
        self.gridLayout_2.addWidget(self.labelWins, 2, 0, 1, 1)
        self.lineEditTotalWins = QtWidgets.QLineEdit(self.groupBoxTotalStats)
        self.lineEditTotalWins.setReadOnly(True)
        self.lineEditTotalWins.setObjectName("lineEditTotalWins")
        self.gridLayout_2.addWidget(self.lineEditTotalWins, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.labelLosses = QtWidgets.QLabel(self.groupBoxTotalStats)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelLosses.setPalette(palette)
        self.labelLosses.setObjectName("labelLosses")
        self.gridLayout_2.addWidget(self.labelLosses, 4, 0, 1, 1)
        self.lineEditTotalLosses = QtWidgets.QLineEdit(self.groupBoxTotalStats)
        self.lineEditTotalLosses.setReadOnly(True)
        self.lineEditTotalLosses.setObjectName("lineEditTotalLosses")
        self.gridLayout_2.addWidget(self.lineEditTotalLosses, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 0, 1, 1)
        self.labelDraws = QtWidgets.QLabel(self.groupBoxTotalStats)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelDraws.setPalette(palette)
        self.labelDraws.setObjectName("labelDraws")
        self.gridLayout_2.addWidget(self.labelDraws, 6, 0, 1, 1)
        self.lineEditTotalDraws = QtWidgets.QLineEdit(self.groupBoxTotalStats)
        self.lineEditTotalDraws.setReadOnly(True)
        self.lineEditTotalDraws.setObjectName("lineEditTotalDraws")
        self.gridLayout_2.addWidget(self.lineEditTotalDraws, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 7, 0, 1, 1)
        self.labelWinrate = QtWidgets.QLabel(self.groupBoxTotalStats)
        self.labelWinrate.setObjectName("labelWinrate")
        self.gridLayout_2.addWidget(self.labelWinrate, 8, 0, 1, 1)
        self.lineEditTotalWinrate = QtWidgets.QLineEdit(self.groupBoxTotalStats)
        self.lineEditTotalWinrate.setReadOnly(True)
        self.lineEditTotalWinrate.setObjectName("lineEditTotalWinrate")
        self.gridLayout_2.addWidget(self.lineEditTotalWinrate, 8, 1, 1, 1)
        self.gridLayoutStats.addWidget(self.groupBoxTotalStats, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayoutStats, 1, 0, 1, 1)
        self.tabWidgetSubsection = QtWidgets.QTabWidget(self.groupBoxStats)
        self.tabWidgetSubsection.setObjectName("tabWidgetSubsection")
        self.qWidgetDaily = QtWidgets.QWidget()
        self.qWidgetDaily.setObjectName("qWidgetDaily")
        self.gridLayout = QtWidgets.QGridLayout(self.qWidgetDaily)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutDaily = QtWidgets.QGridLayout()
        self.gridLayoutDaily.setObjectName("gridLayoutDaily")
        self.labelDailyDraws = QtWidgets.QLabel(self.qWidgetDaily)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelDailyDraws.setPalette(palette)
        self.labelDailyDraws.setObjectName("labelDailyDraws")
        self.gridLayoutDaily.addWidget(self.labelDailyDraws, 5, 0, 1, 1)
        self.labelDailyWins = QtWidgets.QLabel(self.qWidgetDaily)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelDailyWins.setPalette(palette)
        self.labelDailyWins.setObjectName("labelDailyWins")
        self.gridLayoutDaily.addWidget(self.labelDailyWins, 3, 0, 1, 1)
        self.labelDailyWinrate = QtWidgets.QLabel(self.qWidgetDaily)
        self.labelDailyWinrate.setObjectName("labelDailyWinrate")
        self.gridLayoutDaily.addWidget(self.labelDailyWinrate, 6, 0, 1, 1)
        self.labelDailyGames = QtWidgets.QLabel(self.qWidgetDaily)
        self.labelDailyGames.setObjectName("labelDailyGames")
        self.gridLayoutDaily.addWidget(self.labelDailyGames, 1, 0, 1, 1)
        self.labelDailyLosses = QtWidgets.QLabel(self.qWidgetDaily)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelDailyLosses.setPalette(palette)
        self.labelDailyLosses.setObjectName("labelDailyLosses")
        self.gridLayoutDaily.addWidget(self.labelDailyLosses, 4, 0, 1, 1)
        self.lineEditDailyDraws = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyDraws.setReadOnly(True)
        self.lineEditDailyDraws.setObjectName("lineEditDailyDraws")
        self.gridLayoutDaily.addWidget(self.lineEditDailyDraws, 5, 1, 1, 1)
        self.lineEditDailyWins = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyWins.setReadOnly(True)
        self.lineEditDailyWins.setObjectName("lineEditDailyWins")
        self.gridLayoutDaily.addWidget(self.lineEditDailyWins, 3, 1, 1, 1)
        self.lineEditDailyGames = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyGames.setReadOnly(True)
        self.lineEditDailyGames.setObjectName("lineEditDailyGames")
        self.gridLayoutDaily.addWidget(self.lineEditDailyGames, 1, 1, 1, 1)
        self.lineEditDailyRating = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyRating.setObjectName("lineEditDailyRating")
        self.gridLayoutDaily.addWidget(self.lineEditDailyRating, 0, 1, 1, 1)
        self.labelDailyRating = QtWidgets.QLabel(self.qWidgetDaily)
        self.labelDailyRating.setObjectName("labelDailyRating")
        self.gridLayoutDaily.addWidget(self.labelDailyRating, 0, 0, 1, 1)
        self.lineEditDailyLosses = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyLosses.setReadOnly(True)
        self.lineEditDailyLosses.setObjectName("lineEditDailyLosses")
        self.gridLayoutDaily.addWidget(self.lineEditDailyLosses, 4, 1, 1, 1)
        self.lineEditDailyWinrate = QtWidgets.QLineEdit(self.qWidgetDaily)
        self.lineEditDailyWinrate.setReadOnly(True)
        self.lineEditDailyWinrate.setObjectName("lineEditDailyWinrate")
        self.gridLayoutDaily.addWidget(self.lineEditDailyWinrate, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutDaily, 0, 0, 1, 1)
        self.tabWidgetSubsection.addTab(self.qWidgetDaily, "")
        self.qWidgetRapid = QtWidgets.QWidget()
        self.qWidgetRapid.setObjectName("qWidgetRapid")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.qWidgetRapid)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayoutRapid = QtWidgets.QGridLayout()
        self.gridLayoutRapid.setObjectName("gridLayoutRapid")
        self.lineEditRapidDraws = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidDraws.setReadOnly(True)
        self.lineEditRapidDraws.setObjectName("lineEditRapidDraws")
        self.gridLayoutRapid.addWidget(self.lineEditRapidDraws, 5, 1, 1, 1)
        self.lineEditRapidGames = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidGames.setReadOnly(True)
        self.lineEditRapidGames.setObjectName("lineEditRapidGames")
        self.gridLayoutRapid.addWidget(self.lineEditRapidGames, 1, 1, 1, 1)
        self.lineEditRapidLosses = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidLosses.setReadOnly(True)
        self.lineEditRapidLosses.setObjectName("lineEditRapidLosses")
        self.gridLayoutRapid.addWidget(self.lineEditRapidLosses, 4, 1, 1, 1)
        self.lineEditRapidWins = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidWins.setReadOnly(True)
        self.lineEditRapidWins.setObjectName("lineEditRapidWins")
        self.gridLayoutRapid.addWidget(self.lineEditRapidWins, 3, 1, 1, 1)
        self.labelRapidGames = QtWidgets.QLabel(self.qWidgetRapid)
        self.labelRapidGames.setObjectName("labelRapidGames")
        self.gridLayoutRapid.addWidget(self.labelRapidGames, 1, 0, 1, 1)
        self.lineEditRapidWinrate = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidWinrate.setReadOnly(True)
        self.lineEditRapidWinrate.setObjectName("lineEditRapidWinrate")
        self.gridLayoutRapid.addWidget(self.lineEditRapidWinrate, 6, 1, 1, 1)
        self.labelRapidDraws = QtWidgets.QLabel(self.qWidgetRapid)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelRapidDraws.setPalette(palette)
        self.labelRapidDraws.setObjectName("labelRapidDraws")
        self.gridLayoutRapid.addWidget(self.labelRapidDraws, 5, 0, 1, 1)
        self.labelRapidWinrate = QtWidgets.QLabel(self.qWidgetRapid)
        self.labelRapidWinrate.setObjectName("labelRapidWinrate")
        self.gridLayoutRapid.addWidget(self.labelRapidWinrate, 6, 0, 1, 1)
        self.labelRapidWins = QtWidgets.QLabel(self.qWidgetRapid)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelRapidWins.setPalette(palette)
        self.labelRapidWins.setObjectName("labelRapidWins")
        self.gridLayoutRapid.addWidget(self.labelRapidWins, 3, 0, 1, 1)
        self.labelRapidLosses = QtWidgets.QLabel(self.qWidgetRapid)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelRapidLosses.setPalette(palette)
        self.labelRapidLosses.setObjectName("labelRapidLosses")
        self.gridLayoutRapid.addWidget(self.labelRapidLosses, 4, 0, 1, 1)
        self.labelRapidRating = QtWidgets.QLabel(self.qWidgetRapid)
        self.labelRapidRating.setObjectName("labelRapidRating")
        self.gridLayoutRapid.addWidget(self.labelRapidRating, 0, 0, 1, 1)
        self.lineEditRapidRating = QtWidgets.QLineEdit(self.qWidgetRapid)
        self.lineEditRapidRating.setObjectName("lineEditRapidRating")
        self.gridLayoutRapid.addWidget(self.lineEditRapidRating, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayoutRapid, 0, 0, 1, 1)
        self.tabWidgetSubsection.addTab(self.qWidgetRapid, "")
        self.qWidgetBullet = QtWidgets.QWidget()
        self.qWidgetBullet.setObjectName("qWidgetBullet")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.qWidgetBullet)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayoutBullet = QtWidgets.QGridLayout()
        self.gridLayoutBullet.setObjectName("gridLayoutBullet")
        self.labelBulletWinrate = QtWidgets.QLabel(self.qWidgetBullet)
        self.labelBulletWinrate.setObjectName("labelBulletWinrate")
        self.gridLayoutBullet.addWidget(self.labelBulletWinrate, 6, 0, 1, 1)
        self.labelBulletDraws = QtWidgets.QLabel(self.qWidgetBullet)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBulletDraws.setPalette(palette)
        self.labelBulletDraws.setObjectName("labelBulletDraws")
        self.gridLayoutBullet.addWidget(self.labelBulletDraws, 5, 0, 1, 1)
        self.labelBulletWins = QtWidgets.QLabel(self.qWidgetBullet)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBulletWins.setPalette(palette)
        self.labelBulletWins.setObjectName("labelBulletWins")
        self.gridLayoutBullet.addWidget(self.labelBulletWins, 3, 0, 1, 1)
        self.labelBulletGames = QtWidgets.QLabel(self.qWidgetBullet)
        self.labelBulletGames.setObjectName("labelBulletGames")
        self.gridLayoutBullet.addWidget(self.labelBulletGames, 1, 0, 1, 1)
        self.labelBulletLosses = QtWidgets.QLabel(self.qWidgetBullet)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBulletLosses.setPalette(palette)
        self.labelBulletLosses.setObjectName("labelBulletLosses")
        self.gridLayoutBullet.addWidget(self.labelBulletLosses, 4, 0, 1, 1)
        self.lineEditBulletGames = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletGames.setReadOnly(True)
        self.lineEditBulletGames.setObjectName("lineEditBulletGames")
        self.gridLayoutBullet.addWidget(self.lineEditBulletGames, 1, 1, 1, 1)
        self.lineEditBulletWins = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletWins.setReadOnly(True)
        self.lineEditBulletWins.setObjectName("lineEditBulletWins")
        self.gridLayoutBullet.addWidget(self.lineEditBulletWins, 3, 1, 1, 1)
        self.lineEditBulletLosses = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletLosses.setReadOnly(True)
        self.lineEditBulletLosses.setObjectName("lineEditBulletLosses")
        self.gridLayoutBullet.addWidget(self.lineEditBulletLosses, 4, 1, 1, 1)
        self.lineEditBulletDraws = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletDraws.setReadOnly(True)
        self.lineEditBulletDraws.setObjectName("lineEditBulletDraws")
        self.gridLayoutBullet.addWidget(self.lineEditBulletDraws, 5, 1, 1, 1)
        self.lineEditBulletWinrate = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletWinrate.setReadOnly(True)
        self.lineEditBulletWinrate.setObjectName("lineEditBulletWinrate")
        self.gridLayoutBullet.addWidget(self.lineEditBulletWinrate, 6, 1, 1, 1)
        self.labelBulletRating = QtWidgets.QLabel(self.qWidgetBullet)
        self.labelBulletRating.setObjectName("labelBulletRating")
        self.gridLayoutBullet.addWidget(self.labelBulletRating, 0, 0, 1, 1)
        self.lineEditBulletRating = QtWidgets.QLineEdit(self.qWidgetBullet)
        self.lineEditBulletRating.setObjectName("lineEditBulletRating")
        self.gridLayoutBullet.addWidget(self.lineEditBulletRating, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayoutBullet, 0, 0, 1, 1)
        self.tabWidgetSubsection.addTab(self.qWidgetBullet, "")
        self.qWidgetBlitz = QtWidgets.QWidget()
        self.qWidgetBlitz.setObjectName("qWidgetBlitz")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.qWidgetBlitz)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayoutBlitz = QtWidgets.QGridLayout()
        self.gridLayoutBlitz.setObjectName("gridLayoutBlitz")
        self.labelBlitzDraws = QtWidgets.QLabel(self.qWidgetBlitz)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBlitzDraws.setPalette(palette)
        self.labelBlitzDraws.setObjectName("labelBlitzDraws")
        self.gridLayoutBlitz.addWidget(self.labelBlitzDraws, 5, 0, 1, 1)
        self.labelBlitzWinrate = QtWidgets.QLabel(self.qWidgetBlitz)
        self.labelBlitzWinrate.setObjectName("labelBlitzWinrate")
        self.gridLayoutBlitz.addWidget(self.labelBlitzWinrate, 6, 0, 1, 1)
        self.labelBlitzWins = QtWidgets.QLabel(self.qWidgetBlitz)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBlitzWins.setPalette(palette)
        self.labelBlitzWins.setObjectName("labelBlitzWins")
        self.gridLayoutBlitz.addWidget(self.labelBlitzWins, 3, 0, 1, 1)
        self.labelBlitzLosses = QtWidgets.QLabel(self.qWidgetBlitz)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelBlitzLosses.setPalette(palette)
        self.labelBlitzLosses.setObjectName("labelBlitzLosses")
        self.gridLayoutBlitz.addWidget(self.labelBlitzLosses, 4, 0, 1, 1)
        self.lineEditBlitzWinrate = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzWinrate.setReadOnly(True)
        self.lineEditBlitzWinrate.setObjectName("lineEditBlitzWinrate")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzWinrate, 6, 1, 1, 1)
        self.lineEditBlitzDraws = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzDraws.setReadOnly(True)
        self.lineEditBlitzDraws.setObjectName("lineEditBlitzDraws")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzDraws, 5, 1, 1, 1)
        self.labelBlitzGames = QtWidgets.QLabel(self.qWidgetBlitz)
        self.labelBlitzGames.setObjectName("labelBlitzGames")
        self.gridLayoutBlitz.addWidget(self.labelBlitzGames, 1, 0, 1, 1)
        self.lineEditBlitzGames = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzGames.setReadOnly(True)
        self.lineEditBlitzGames.setObjectName("lineEditBlitzGames")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzGames, 1, 1, 1, 1)
        self.lineEditBlitzWins = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzWins.setReadOnly(True)
        self.lineEditBlitzWins.setObjectName("lineEditBlitzWins")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzWins, 3, 1, 1, 1)
        self.lineEditBlitzLosses = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzLosses.setReadOnly(True)
        self.lineEditBlitzLosses.setObjectName("lineEditBlitzLosses")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzLosses, 4, 1, 1, 1)
        self.labelBlitzRating = QtWidgets.QLabel(self.qWidgetBlitz)
        self.labelBlitzRating.setObjectName("labelBlitzRating")
        self.gridLayoutBlitz.addWidget(self.labelBlitzRating, 0, 0, 1, 1)
        self.lineEditBlitzRating = QtWidgets.QLineEdit(self.qWidgetBlitz)
        self.lineEditBlitzRating.setObjectName("lineEditBlitzRating")
        self.gridLayoutBlitz.addWidget(self.lineEditBlitzRating, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayoutBlitz, 0, 0, 1, 1)
        self.tabWidgetSubsection.addTab(self.qWidgetBlitz, "")
        self.gridLayout_5.addWidget(self.tabWidgetSubsection, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBoxStats)
        self.groupBoxProfile = QtWidgets.QGroupBox(self.qWidgetPlayer)
        self.groupBoxProfile.setObjectName("groupBoxProfile")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxProfile)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayoutProfile = QtWidgets.QGridLayout()
        self.gridLayoutProfile.setObjectName("gridLayoutProfile")
        self.lineEditFollowers = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditFollowers.setReadOnly(True)
        self.lineEditFollowers.setObjectName("lineEditFollowers")
        self.gridLayoutProfile.addWidget(self.lineEditFollowers, 0, 1, 1, 1)
        self.lineEditTitle = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditTitle.setReadOnly(True)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.gridLayoutProfile.addWidget(self.lineEditTitle, 2, 1, 1, 1)
        self.labelLastOnline = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelLastOnline.setObjectName("labelLastOnline")
        self.gridLayoutProfile.addWidget(self.labelLastOnline, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem4, 5, 0, 1, 1)
        self.labelFollowers = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelFollowers.setObjectName("labelFollowers")
        self.gridLayoutProfile.addWidget(self.labelFollowers, 0, 0, 1, 1)
        self.labelJoinedOn = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelJoinedOn.setObjectName("labelJoinedOn")
        self.gridLayoutProfile.addWidget(self.labelJoinedOn, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem5, 7, 0, 1, 1)
        self.labelName = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelName.setObjectName("labelName")
        self.gridLayoutProfile.addWidget(self.labelName, 10, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBoxProfile)
        self.label.setObjectName("label")
        self.gridLayoutProfile.addWidget(self.label, 12, 0, 1, 1)
        self.labelUsername = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayoutProfile.addWidget(self.labelUsername, 8, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem6, 9, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem7, 11, 0, 1, 1)
        self.labelTitle = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayoutProfile.addWidget(self.labelTitle, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutProfile.addItem(spacerItem9, 3, 0, 1, 1)
        self.lineEditLastOnline = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditLastOnline.setReadOnly(True)
        self.lineEditLastOnline.setObjectName("lineEditLastOnline")
        self.gridLayoutProfile.addWidget(self.lineEditLastOnline, 4, 1, 1, 1)
        self.lineEditJoinedOn = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditJoinedOn.setReadOnly(True)
        self.lineEditJoinedOn.setObjectName("lineEditJoinedOn")
        self.gridLayoutProfile.addWidget(self.lineEditJoinedOn, 6, 1, 1, 1)
        self.lineEditUsername = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditUsername.setReadOnly(True)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayoutProfile.addWidget(self.lineEditUsername, 8, 1, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditName.setReadOnly(True)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayoutProfile.addWidget(self.lineEditName, 10, 1, 1, 1)
        self.lineEditStatus = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditStatus.setReadOnly(True)
        self.lineEditStatus.setObjectName("lineEditStatus")
        self.gridLayoutProfile.addWidget(self.lineEditStatus, 12, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayoutProfile, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBoxProfile)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.tabWidget.addTab(self.qWidgetPlayer, "")
        self.qWidgetLeaderboard = QtWidgets.QWidget()
        self.qWidgetLeaderboard.setObjectName("qWidgetLeaderboard")
        self.tabWidget.addTab(self.qWidgetLeaderboard, "")
        self.horizontalLayoutMain.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayoutMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidgetSubsection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPlayerSearch.setText(_translate("MainWindow", "Search"))
        self.groupBoxStats.setTitle(_translate("MainWindow", "Stats"))
        self.groupBoxTotalStats.setTitle(_translate("MainWindow", "Total"))
        self.labelGames.setText(_translate("MainWindow", "Games"))
        self.labelWins.setText(_translate("MainWindow", "Wins"))
        self.labelLosses.setText(_translate("MainWindow", "Losses"))
        self.labelDraws.setText(_translate("MainWindow", "Draws"))
        self.labelWinrate.setText(_translate("MainWindow", "Win %"))
        self.labelDailyDraws.setText(_translate("MainWindow", "Draws"))
        self.labelDailyWins.setText(_translate("MainWindow", "Wins"))
        self.labelDailyWinrate.setText(_translate("MainWindow", "Win %"))
        self.labelDailyGames.setText(_translate("MainWindow", "Games"))
        self.labelDailyLosses.setText(_translate("MainWindow", "Losses"))
        self.labelDailyRating.setText(_translate("MainWindow", "Rating"))
        self.tabWidgetSubsection.setTabText(self.tabWidgetSubsection.indexOf(self.qWidgetDaily), _translate("MainWindow", "Daily"))
        self.labelRapidGames.setText(_translate("MainWindow", "Games"))
        self.labelRapidDraws.setText(_translate("MainWindow", "Draws"))
        self.labelRapidWinrate.setText(_translate("MainWindow", "Win %"))
        self.labelRapidWins.setText(_translate("MainWindow", "Wins"))
        self.labelRapidLosses.setText(_translate("MainWindow", "Losses"))
        self.labelRapidRating.setText(_translate("MainWindow", "Rating"))
        self.tabWidgetSubsection.setTabText(self.tabWidgetSubsection.indexOf(self.qWidgetRapid), _translate("MainWindow", "Rapid"))
        self.labelBulletWinrate.setText(_translate("MainWindow", "Win %"))
        self.labelBulletDraws.setText(_translate("MainWindow", "Draws"))
        self.labelBulletWins.setText(_translate("MainWindow", "Wins"))
        self.labelBulletGames.setText(_translate("MainWindow", "Games"))
        self.labelBulletLosses.setText(_translate("MainWindow", "Losses"))
        self.labelBulletRating.setText(_translate("MainWindow", "Rating"))
        self.tabWidgetSubsection.setTabText(self.tabWidgetSubsection.indexOf(self.qWidgetBullet), _translate("MainWindow", "Bullet"))
        self.labelBlitzDraws.setText(_translate("MainWindow", "Draws"))
        self.labelBlitzWinrate.setText(_translate("MainWindow", "Win %"))
        self.labelBlitzWins.setText(_translate("MainWindow", "Wins"))
        self.labelBlitzLosses.setText(_translate("MainWindow", "Losses"))
        self.labelBlitzGames.setText(_translate("MainWindow", "Games"))
        self.labelBlitzRating.setText(_translate("MainWindow", "Rating"))
        self.tabWidgetSubsection.setTabText(self.tabWidgetSubsection.indexOf(self.qWidgetBlitz), _translate("MainWindow", "Blitz"))
        self.groupBoxProfile.setTitle(_translate("MainWindow", "Profile"))
        self.labelLastOnline.setText(_translate("MainWindow", "Last online"))
        self.labelFollowers.setText(_translate("MainWindow", "Followers"))
        self.labelJoinedOn.setText(_translate("MainWindow", "Joined on"))
        self.labelName.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "Status"))
        self.labelUsername.setText(_translate("MainWindow", "Username"))
        self.labelTitle.setText(_translate("MainWindow", "Title"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qWidgetPlayer), _translate("MainWindow", "Player"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qWidgetLeaderboard), _translate("MainWindow", "Leaderboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
