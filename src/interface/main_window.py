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
        MainWindow.resize(800, 600)
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
        self.qWidgetPlayer.setObjectName("qWidgetPlayer")
        self.lineEditPlayerSearch = QtWidgets.QLineEdit(self.qWidgetPlayer)
        self.lineEditPlayerSearch.setGeometry(QtCore.QRect(20, 20, 241, 21))
        self.lineEditPlayerSearch.setObjectName("lineEditPlayerSearch")
        self.pushButtonPlayerSearch = QtWidgets.QPushButton(self.qWidgetPlayer)
        self.pushButtonPlayerSearch.setGeometry(QtCore.QRect(270, 12, 81, 41))
        self.pushButtonPlayerSearch.setObjectName("pushButtonPlayerSearch")
        self.groupBoxStats = QtWidgets.QGroupBox(self.qWidgetPlayer)
        self.groupBoxStats.setGeometry(QtCore.QRect(20, 60, 331, 441))
        self.groupBoxStats.setObjectName("groupBoxStats")
        self.labelGames = QtWidgets.QLabel(self.groupBoxStats)
        self.labelGames.setGeometry(QtCore.QRect(90, 10, 51, 16))
        self.labelGames.setObjectName("labelGames")
        self.lineEditGames = QtWidgets.QLineEdit(self.groupBoxStats)
        self.lineEditGames.setGeometry(QtCore.QRect(160, 10, 113, 20))
        self.lineEditGames.setObjectName("lineEditGames")
        self.lineStats = QtWidgets.QFrame(self.groupBoxStats)
        self.lineStats.setGeometry(QtCore.QRect(20, 40, 291, 16))
        self.lineStats.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineStats.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineStats.setObjectName("lineStats")
        self.labelWins = QtWidgets.QLabel(self.groupBoxStats)
        self.labelWins.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.labelWins.setObjectName("labelWins")
        self.labelLosses = QtWidgets.QLabel(self.groupBoxStats)
        self.labelLosses.setGeometry(QtCore.QRect(150, 60, 47, 21))
        self.labelLosses.setObjectName("labelLosses")
        self.labelDraws = QtWidgets.QLabel(self.groupBoxStats)
        self.labelDraws.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.labelDraws.setObjectName("labelDraws")
        self.labelWinrate = QtWidgets.QLabel(self.groupBoxStats)
        self.labelWinrate.setGeometry(QtCore.QRect(150, 90, 47, 16))
        self.labelWinrate.setObjectName("labelWinrate")
        self.groupBoxProfile = QtWidgets.QGroupBox(self.qWidgetPlayer)
        self.groupBoxProfile.setGeometry(QtCore.QRect(360, 10, 401, 491))
        self.groupBoxProfile.setObjectName("groupBoxProfile")
        self.labelName = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.labelName.setObjectName("labelName")
        self.labelUsername = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelUsername.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.labelUsername.setObjectName("labelUsername")
        self.labelTitle = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelTitle.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.labelTitle.setObjectName("labelTitle")
        self.labelFollowers = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelFollowers.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.labelFollowers.setObjectName("labelFollowers")
        self.labelLastOnline = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelLastOnline.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.labelLastOnline.setObjectName("labelLastOnline")
        self.labelJoinedOn = QtWidgets.QLabel(self.groupBoxProfile)
        self.labelJoinedOn.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.labelJoinedOn.setObjectName("labelJoinedOn")
        self.label = QtWidgets.QLabel(self.groupBoxProfile)
        self.label.setGeometry(QtCore.QRect(20, 200, 91, 21))
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditName.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditUsername = QtWidgets.QLineEdit(self.groupBoxProfile)
        self.lineEditUsername.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.tabWidget.addTab(self.qWidgetPlayer, "")
        self.qWidgetLeaderboard = QtWidgets.QWidget()
        self.qWidgetLeaderboard.setObjectName("qWidgetLeaderboard")
        self.tabWidget.addTab(self.qWidgetLeaderboard, "")
        self.horizontalLayoutMain.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayoutMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.labelName.setText(_translate("MainWindow", "Name"))
        self.labelUsername.setText(_translate("MainWindow", "Username"))
        self.labelTitle.setText(_translate("MainWindow", "Title"))
        self.labelFollowers.setText(_translate("MainWindow", "Followers"))
        self.labelLastOnline.setText(_translate("MainWindow", "Last online"))
        self.labelJoinedOn.setText(_translate("MainWindow", "Joined on"))
        self.label.setText(_translate("MainWindow", "Status"))
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
