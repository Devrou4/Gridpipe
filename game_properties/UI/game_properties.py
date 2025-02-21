# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_properties.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: rgb(63, 71, 56);\n"
"border-radius: 15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(63, 71, 56, 255), stop:0.610734 rgba(70, 70, 70, 255));\n"
"}")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.lb_gamename = QLabel(self.f_titlebar)
        self.lb_gamename.setObjectName(u"lb_gamename")
        self.lb_gamename.setStyleSheet(u"color: rgb(216, 222, 211);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.lb_gamename)

        self.LB_properties = QLabel(self.f_titlebar)
        self.LB_properties.setObjectName(u"LB_properties")
        self.LB_properties.setStyleSheet(u"color: rgb(216, 222, 211);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.LB_properties)

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
        self.pb_min.setStyleSheet(u"QPushButton{\n"
"	image: url(:/buttons/buttons/Window-Min.png);\n"
"}\n"
"QPushButton:hover{\n"
"	image: url(:/buttons/buttons/Window-Min-Hover.png);\n"
"}")

        self.horizontalLayout.addWidget(self.pb_min)

        self.pb_close = QPushButton(self.f_titlebar)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMaximumSize(QSize(16, 16))
        self.pb_close.setStyleSheet(u"QPushButton{\n"
"	image: url(:/buttons/buttons/Window-Close.tga);\n"
"}\n"
"QPushButton::hover{\n"
"	image: url(:/buttons/buttons/Window-Close-Hover.png);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pb_close)


        self.gridLayout_3.addWidget(self.f_titlebar, 0, 0, 1, 2)

        self.fr_buttons = QFrame(self.centralwidget)
        self.fr_buttons.setObjectName(u"fr_buttons")
        self.fr_buttons.setMinimumSize(QSize(0, 44))
        self.fr_buttons.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.fr_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.pb_uninstall = QPushButton(self.fr_buttons)
        self.pb_uninstall.setObjectName(u"pb_uninstall")
        self.pb_uninstall.setMinimumSize(QSize(70, 24))
        self.pb_uninstall.setMaximumSize(QSize(16777215, 24))
        self.pb_uninstall.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pb_uninstall)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pb_close_2 = QPushButton(self.fr_buttons)
        self.pb_close_2.setObjectName(u"pb_close_2")
        self.pb_close_2.setMinimumSize(QSize(100, 24))
        self.pb_close_2.setMaximumSize(QSize(16777215, 24))
        self.pb_close_2.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pb_close_2)


        self.gridLayout_3.addWidget(self.fr_buttons, 2, 1, 1, 1)

        self.tw_tabs = QTabWidget(self.centralwidget)
        self.tw_tabs.setObjectName(u"tw_tabs")
        self.tw_tabs.setAutoFillBackground(False)
        self.tw_tabs.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(101, 106, 98);\n"
"} \n"
"QTabWidget::pane {\n"
"    background-color: #f0f0f0;  /* Light grey background */\n"
"	border: 3px solid #686a65;\n"
"	border-top: 3px solid #686a65;\n"
"	border-left: 3px solid qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.92605 rgba(104, 106, 101, 255), stop:1 rgba(94, 92, 89, 255));\n"
"	border-right: 3px solid qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.92605 rgba(104, 106, 101, 255), stop:1 rgba(94, 92, 89, 255));\n"
"	border-bottom: 2px solid rgb(94,92,89);\n"
"	\n"
"	\n"
"	border-top-right-radius: 5px; \n"
"	border-bottom-right-radius: 5px; \n"
"	border-bottom-left-radius: 5px; \n"
"	margin-left: 3px;\n"
"	margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgb(81, 89, 76);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px; \n"
"	padding: 5px;\n"
"	margin-right: 3px;\n"
"	margin-left: 3px;\n"
"	widt"
                        "h: 96px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  	\n"
"	background-color: rgb(104, 106, 101);\n"
"	color: rgb(196, 181, 80);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	\n"
"\n"
"}")
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.tab_general.setStyleSheet(u"#tab_general{\n"
"	background-color: rgb(104, 106, 101);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.92605 rgba(104, 106, 101, 255), stop:1 rgba(94, 92, 89, 255));\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.tab_general)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, -1, 25, -1)
        self.lb_developer = QLabel(self.tab_general)
        self.lb_developer.setObjectName(u"lb_developer")
        self.lb_developer.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_2.addWidget(self.lb_developer, 1, 1, 1, 1)

        self.lb_manual = QLabel(self.tab_general)
        self.lb_manual.setObjectName(u"lb_manual")
        self.lb_manual.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_2.addWidget(self.lb_manual, 2, 1, 1, 1)

        self.line_line = QFrame(self.tab_general)
        self.line_line.setObjectName(u"line_line")
        self.line_line.setStyleSheet(u"Line{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.line_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_line.setLineWidth(3)
        self.line_line.setMidLineWidth(0)
        self.line_line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_2.addWidget(self.line_line, 3, 0, 1, 2)

        self.LB_developer = QLabel(self.tab_general)
        self.LB_developer.setObjectName(u"LB_developer")
        self.LB_developer.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")

        self.gridLayout_2.addWidget(self.LB_developer, 1, 0, 1, 1)

        self.lb_homepage = QLabel(self.tab_general)
        self.lb_homepage.setObjectName(u"lb_homepage")
        self.lb_homepage.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_2.addWidget(self.lb_homepage, 0, 1, 1, 1)

        self.LB_manual = QLabel(self.tab_general)
        self.LB_manual.setObjectName(u"LB_manual")
        self.LB_manual.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")

        self.gridLayout_2.addWidget(self.LB_manual, 2, 0, 1, 1)

        self.LB_homepage = QLabel(self.tab_general)
        self.LB_homepage.setObjectName(u"LB_homepage")
        self.LB_homepage.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")

        self.gridLayout_2.addWidget(self.LB_homepage, 0, 0, 1, 1)

        self.wg_buttons = QWidget(self.tab_general)
        self.wg_buttons.setObjectName(u"wg_buttons")
        self.wg_buttons.setMinimumSize(QSize(0, 140))
        self.wg_buttons.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout = QVBoxLayout(self.wg_buttons)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.pb_shortcut = QPushButton(self.wg_buttons)
        self.pb_shortcut.setObjectName(u"pb_shortcut")
        self.pb_shortcut.setMaximumSize(QSize(230, 16777215))
        self.pb_shortcut.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")

        self.verticalLayout.addWidget(self.pb_shortcut)

        self.pb_args = QPushButton(self.wg_buttons)
        self.pb_args.setObjectName(u"pb_args")
        self.pb_args.setMaximumSize(QSize(230, 16777215))
        self.pb_args.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")

        self.verticalLayout.addWidget(self.pb_args)


        self.gridLayout_2.addWidget(self.wg_buttons, 4, 0, 1, 2)

        self.tw_tabs.addTab(self.tab_general, "")
        self.tab_updates = QWidget()
        self.tab_updates.setObjectName(u"tab_updates")
        self.tab_updates.setStyleSheet(u"#tab_updates{\n"
"	background-color: rgb(104, 106, 101);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.92605 rgba(104, 106, 101, 255), stop:1 rgba(94, 92, 89, 255));\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.tab_updates)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(25, -1, 25, -1)
        self.lb_autoupdates = QLabel(self.tab_updates)
        self.lb_autoupdates.setObjectName(u"lb_autoupdates")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_autoupdates.sizePolicy().hasHeightForWidth())
        self.lb_autoupdates.setSizePolicy(sizePolicy1)
        self.lb_autoupdates.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	margin-top: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.lb_autoupdates, 0, 0, 1, 1)

        self.cb_updates = QComboBox(self.tab_updates)
        self.cb_updates.addItem("")
        self.cb_updates.setObjectName(u"cb_updates")
        self.cb_updates.setStyleSheet(u"QComboBox {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.cb_updates, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tab_updates)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.label_2.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.lb_history = QLabel(self.tab_updates)
        self.lb_history.setObjectName(u"lb_history")
        self.lb_history.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_4.addWidget(self.lb_history, 3, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_updates, "")
        self.tab_files = QWidget()
        self.tab_files.setObjectName(u"tab_files")
        self.tab_files.setStyleSheet(u"#tab_files{\n"
"	background-color: rgb(104, 106, 101);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.92605 rgba(104, 106, 101, 255), stop:1 rgba(94, 92, 89, 255));\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.tab_files)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(25, -1, 25, -1)
        self.label = QLabel(self.tab_files)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	margin-top: 15px;\n"
"}")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_files)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(216, 222, 211);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	margin-top: 15px;\n"
"}")

        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)

        self.wg_buttons_2 = QWidget(self.tab_files)
        self.wg_buttons_2.setObjectName(u"wg_buttons_2")
        self.pushButton = QPushButton(self.wg_buttons_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 70, 256, 24))
        self.pushButton.setMinimumSize(QSize(256, 0))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")
        self.pushButton_2 = QPushButton(self.wg_buttons_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 40, 256, 24))
        self.pushButton_2.setMinimumSize(QSize(256, 0))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")
        self.pushButton_4 = QPushButton(self.wg_buttons_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 100, 256, 24))
        self.pushButton_4.setMinimumSize(QSize(256, 0))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:  #7b7e7a;\n"
"    background: transparent;\n"
"    background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat; /* Prevent tiling */\n"
"    border: 3px solid #7b7e7a ; /* Remove button borders to match the image */\n"
"	border-radius: 8px;\n"
"	padding: 3px;\n"
"}")

        self.gridLayout_5.addWidget(self.wg_buttons_2, 1, 0, 1, 2)

        self.tw_tabs.addTab(self.tab_files, "")

        self.gridLayout_3.addWidget(self.tw_tabs, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tw_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lb_gamename.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">GRIDPIPE</span></p></body></html>", None))
        self.LB_properties.setText(QCoreApplication.translate("Dialog", u"- Properties", None))
        self.pb_min.setText("")
        self.pb_close.setText("")
        self.pb_uninstall.setText(QCoreApplication.translate("Dialog", u"Uninstall", None))
        self.pb_close_2.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.lb_developer.setText(QCoreApplication.translate("Dialog", u"dev", None))
        self.lb_manual.setText(QCoreApplication.translate("Dialog", u"man", None))
        self.LB_developer.setText(QCoreApplication.translate("Dialog", u"Developer", None))
        self.lb_homepage.setText(QCoreApplication.translate("Dialog", u"url", None))
        self.LB_manual.setText(QCoreApplication.translate("Dialog", u"Manual", None))
        self.LB_homepage.setText(QCoreApplication.translate("Dialog", u"Homepage", None))
        self.pb_shortcut.setText(QCoreApplication.translate("Dialog", u"Create desktop shortcut", None))
        self.pb_args.setText(QCoreApplication.translate("Dialog", u"Set launch options...", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_general), QCoreApplication.translate("Dialog", u"General", None))
        self.lb_autoupdates.setText(QCoreApplication.translate("Dialog", u"Automatic updates", None))
        self.cb_updates.setItemText(0, QCoreApplication.translate("Dialog", u"Do not automatically update this game", None))

        self.cb_updates.setCurrentText(QCoreApplication.translate("Dialog", u"Do not automatically update this game", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"(Content for this game will not be automatically acquired.)", None))
        self.lb_history.setText(QCoreApplication.translate("Dialog", u"update history", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_updates), QCoreApplication.translate("Dialog", u"Updates", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Disk usage", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"< none >", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Delete local game content...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Backup game files...", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Verify integrity of game cache...", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_files), QCoreApplication.translate("Dialog", u"Local files", None))
    # retranslateUi

