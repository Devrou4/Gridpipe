# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: rgb(63, 71, 56);\n"
"border-radius: 15px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.f_titlebar = QFrame(self.centralwidget)
        self.f_titlebar.setObjectName(u"f_titlebar")
        self.f_titlebar.setStyleSheet(u"background-color: rgb(90, 106, 80);\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px; \n"
"color: rgb(255, 255, 255);")
        self.f_titlebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_titlebar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_titlebar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 3, 9, 6)
        self.fakepb_icon = QPushButton(self.f_titlebar)
        self.fakepb_icon.setObjectName(u"fakepb_icon")
        icon = QIcon()
        icon.addFile(u":/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fakepb_icon.setIcon(icon)
        self.fakepb_icon.setFlat(True)

        self.horizontalLayout.addWidget(self.fakepb_icon)

        self.lb_title = QLabel(self.f_titlebar)
        self.lb_title.setObjectName(u"lb_title")

        self.horizontalLayout.addWidget(self.lb_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_min = QPushButton(self.f_titlebar)
        self.pb_min.setObjectName(u"pb_min")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_min.sizePolicy().hasHeightForWidth())
        self.pb_min.setSizePolicy(sizePolicy)
        self.pb_min.setMaximumSize(QSize(16, 16))
        self.pb_min.setStyleSheet(u"image: url(:/buttons/buttons/Window-Min.png);")

        self.horizontalLayout.addWidget(self.pb_min)

        self.pb_close = QPushButton(self.f_titlebar)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMaximumSize(QSize(16, 16))
        self.pb_close.setStyleSheet(u"image: url(:/buttons/buttons/Window-Close.tga);\n"
"")

        self.horizontalLayout.addWidget(self.pb_close)


        self.gridLayout.addWidget(self.f_titlebar, 0, 0, 1, 1)

        self.tw_tabs = QTabWidget(self.centralwidget)
        self.tw_tabs.setObjectName(u"tw_tabs")
        self.tw_tabs.setAutoFillBackground(False)
        self.tw_tabs.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(101, 106, 98);\n"
"} \n"
"QTabWidget::pane {\n"
"    background-color: #f0f0f0;  /* Light grey background */\n"
"	border: 3px solid #656a62;\n"
"	border-top-right-radius: 5px; \n"
"	border-bottom-right-radius: 5px; \n"
"	border-bottom-left-radius: 5px; \n"
"	margin-left: 3px;\n"
"	margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgb(81, 89, 76);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px; \n"
"	padding: 5px;\n"
"	margin-right: 3px;\n"
"	margin-left: 3px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  	\n"
"	background-color: rgb(101, 106, 98);\n"
"	color: rgb(150, 135, 50);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	\n"
"\n"
"}")
        self.tab_games = QWidget()
        self.tab_games.setObjectName(u"tab_games")
        self.tab_games.setStyleSheet(u"background-color: rgb(101, 106, 98);")
        self.gridLayout_2 = QGridLayout(self.tab_games)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(self.tab_games)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding:1px;")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding:1px;")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.tbl_games = QTableWidget(self.tab_games)
        if (self.tbl_games.columnCount() < 4):
            self.tbl_games.setColumnCount(4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.HorPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tbl_games.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_games.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_games.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_games.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tbl_games.rowCount() < 4):
            self.tbl_games.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_games.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_games.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_games.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_games.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_games.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_games.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_games.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_games.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_games.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_games.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_games.setItem(3, 0, __qtablewidgetitem14)
        self.tbl_games.setObjectName(u"tbl_games")
        self.tbl_games.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(70, 78, 71);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border: none;\n"
"	selection-background-color: transparent;\n"
"	outline: none;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(101, 106, 98);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-top: none;\n"
"	border-right:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(101, 106, 98);\n"
"\n"
"}\n"
"QTableWidget::item {\n"
"	background-color: rgb(70, 78, 71);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:selected {\n"
"    \n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;    \n"
"    outline: none; \n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    outline: none;  /* Remove focus outline */\n"
"}\n"
"")
        self.tbl_games.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_games.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_games.setShowGrid(False)
        self.tbl_games.setGridStyle(Qt.PenStyle.NoPen)
        self.tbl_games.setSortingEnabled(True)
        self.tbl_games.setCornerButtonEnabled(True)
        self.tbl_games.horizontalHeader().setVisible(True)
        self.tbl_games.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_games.horizontalHeader().setMinimumSectionSize(60)
        self.tbl_games.horizontalHeader().setDefaultSectionSize(120)
        self.tbl_games.horizontalHeader().setHighlightSections(False)
        self.tbl_games.horizontalHeader().setStretchLastSection(True)
        self.tbl_games.verticalHeader().setVisible(False)
        self.tbl_games.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_games.verticalHeader().setHighlightSections(False)

        self.gridLayout_2.addWidget(self.tbl_games, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_games, "")
        self.tab_tools = QWidget()
        self.tab_tools.setObjectName(u"tab_tools")
        self.tw_tabs.addTab(self.tab_tools, "")

        self.gridLayout.addWidget(self.tw_tabs, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tw_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fakepb_icon.setText("")
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">GRIDPIPE</span></p></body></html>", None))
        self.pb_min.setText("")
        self.pb_close.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        ___qtablewidgetitem = self.tbl_games.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Games", None));
        ___qtablewidgetitem1 = self.tbl_games.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem2 = self.tbl_games.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Year Released", None));
        ___qtablewidgetitem3 = self.tbl_games.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Developer", None));

        __sortingEnabled = self.tbl_games.isSortingEnabled()
        self.tbl_games.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tbl_games.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Game 1", None));
        ___qtablewidgetitem5 = self.tbl_games.item(1, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Game 2", None));
        ___qtablewidgetitem6 = self.tbl_games.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Game 3", None));
        ___qtablewidgetitem7 = self.tbl_games.item(3, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Game 4", None));
        self.tbl_games.setSortingEnabled(__sortingEnabled)

        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_games), QCoreApplication.translate("MainWindow", u"My games", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_tools), QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

