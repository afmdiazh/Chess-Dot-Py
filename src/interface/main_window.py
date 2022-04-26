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
        MainWindow.resize(515, 457)
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
        self.labelGames = QtWidgets.QLabel(self.groupBoxStats)
        self.labelGames.setObjectName("labelGames")
        self.gridLayoutStats.addWidget(self.labelGames, 0, 0, 1, 1)
        self.lineEditGames = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditGames.setReadOnly(True)
        self.lineEditGames.setObjectName("lineEditGames")
        self.gridLayoutStats.addWidget(self.lineEditGames, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutStats.addItem(spacerItem, 1, 0, 1, 1)
        self.labelWins = QtWidgets.QLabel(self.groupBoxStats)
        self.labelWins.setObjectName("labelWins")
        self.gridLayoutStats.addWidget(self.labelWins, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutStats.addItem(spacerItem1, 3, 0, 1, 1)
        self.labelLosses = QtWidgets.QLabel(self.groupBoxStats)
        self.labelLosses.setObjectName("labelLosses")
        self.gridLayoutStats.addWidget(self.labelLosses, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutStats.addItem(spacerItem2, 5, 0, 1, 1)
        self.labelDraws = QtWidgets.QLabel(self.groupBoxStats)
        self.labelDraws.setObjectName("labelDraws")
        self.gridLayoutStats.addWidget(self.labelDraws, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutStats.addItem(spacerItem3, 7, 0, 1, 1)
        self.labelWinrate = QtWidgets.QLabel(self.groupBoxStats)
        self.labelWinrate.setObjectName("labelWinrate")
        self.gridLayoutStats.addWidget(self.labelWinrate, 8, 0, 1, 1)
        self.lineEditWins = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditWins.setReadOnly(True)
        self.lineEditWins.setObjectName("lineEditWins")
        self.gridLayoutStats.addWidget(self.lineEditWins, 2, 1, 1, 1)
        self.lineEditLosses = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditLosses.setReadOnly(True)
        self.lineEditLosses.setObjectName("lineEditLosses")
        self.gridLayoutStats.addWidget(self.lineEditLosses, 4, 1, 1, 1)
        self.lineEditDraws = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditDraws.setReadOnly(True)
        self.lineEditDraws.setObjectName("lineEditDraws")
        self.gridLayoutStats.addWidget(self.lineEditDraws, 6, 1, 1, 1)
        self.lineEditWinrate = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditWinrate.setReadOnly(True)
        self.lineEditWinrate.setObjectName("lineEditWinrate")
        self.gridLayoutStats.addWidget(self.lineEditWinrate, 8, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayoutStats, 0, 0, 1, 1)
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
        self.gridLayout_4.addLayout(self.gridLayoutProfile, 0, 0, 1, 1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPlayerSearch.setText(_translate("MainWindow", "Search"))
        self.labelGames.setText(_translate("MainWindow", "Games"))
        self.labelWins.setText(_translate("MainWindow", "Wins"))
        self.labelLosses.setText(_translate("MainWindow", "Losses"))
        self.labelDraws.setText(_translate("MainWindow", "Draws"))
        self.labelWinrate.setText(_translate("MainWindow", "Win %"))
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
