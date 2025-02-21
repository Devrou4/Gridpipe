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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)
import assets_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: rgb(63, 71, 56);\n"
"border-radius: 15px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
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
        self.lb_title.setStyleSheet(u"color: rgb(216, 222, 211);")

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


        self.gridLayout_3.addWidget(self.f_titlebar, 1, 0, 1, 2)

        self.f_buttons = QFrame(self.centralwidget)
        self.f_buttons.setObjectName(u"f_buttons")
        self.f_buttons.setMinimumSize(QSize(0, 45))
        self.f_buttons.setStyleSheet(u"background-color: rgb(90, 106, 80);\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 15px; \n"
"color: rgb(255, 255, 255);")
        self.f_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.pushButton = QPushButton(self.f_buttons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 0))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding:1px;")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pb_ok = QPushButton(self.f_buttons)
        self.pb_ok.setObjectName(u"pb_ok")
        self.pb_ok.setMinimumSize(QSize(80, 0))
        self.pb_ok.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding:1px;")

        self.horizontalLayout_2.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(self.f_buttons)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setMinimumSize(QSize(80, 0))
        self.pb_cancel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding:1px;")

        self.horizontalLayout_2.addWidget(self.pb_cancel)


        self.gridLayout_3.addWidget(self.f_buttons, 4, 0, 2, 2)

        self.f_content = QFrame(self.centralwidget)
        self.f_content.setObjectName(u"f_content")
        self.f_content.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.f_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_content.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.f_content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_dir = QLineEdit(self.f_content)
        self.le_dir.setObjectName(u"le_dir")

        self.gridLayout_2.addWidget(self.le_dir, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.tb_exe = QToolButton(self.f_content)
        self.tb_exe.setObjectName(u"tb_exe")

        self.gridLayout_2.addWidget(self.tb_exe, 3, 2, 1, 1)

        self.label = QLabel(self.f_content)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 2)

        self.label_2 = QLabel(self.f_content)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.le_exe = QLineEdit(self.f_content)
        self.le_exe.setObjectName(u"le_exe")

        self.gridLayout_2.addWidget(self.le_exe, 3, 1, 1, 1)

        self.tb_dir = QToolButton(self.f_content)
        self.tb_dir.setObjectName(u"tb_dir")

        self.gridLayout_2.addWidget(self.tb_dir, 2, 2, 1, 1)

        self.label_3 = QLabel(self.f_content)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_name = QLineEdit(self.f_content)
        self.le_name.setObjectName(u"le_name")

        self.gridLayout_2.addWidget(self.le_name, 1, 1, 1, 2)


        self.gridLayout_3.addWidget(self.f_content, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.fakepb_icon.setText("")
        self.lb_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">GRIDPIPE</span></p></body></html>", None))
        self.pb_min.setText("")
        self.pb_close.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Uninstall", None))
        self.pb_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.tb_exe.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Game Directory:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Game Exe:", None))
        self.tb_dir.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Game Name:", None))
    # retranslateUi

