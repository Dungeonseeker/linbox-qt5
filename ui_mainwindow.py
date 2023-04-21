# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QListWidget,
                               QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QVBoxLayout, QWidget)



class Ui_MainWindow(object):
    def setupui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(640, 480)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        lin_icon = QIcon()
        lin_icon.addFile(u"./resources/computer_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(lin_icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(10)
        font.setBold(False)
        self.centralwidget.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 621, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.run_btn = QPushButton(self.gridLayoutWidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setEnabled(False)
        icon = QIcon()
        icon.addFile(u"./resources/play_arrow_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.run_btn.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.run_btn)
        self.settings_btn = QPushButton(self.gridLayoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u"./resources/settings_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon1)
        self.horizontalLayout_2.addWidget(self.settings_btn)
        self.create_btn = QPushButton(self.gridLayoutWidget)
        self.create_btn.setObjectName(u"create_btn")
        icon2 = QIcon()
        icon2.addFile(u"./resources/create_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_btn.setIcon(icon2)
        self.horizontalLayout_2.addWidget(self.create_btn)
        self.quit_btn = QPushButton(self.gridLayoutWidget)
        self.quit_btn.setObjectName(u"quit_btn")
        icon3 = QIcon()
        icon3.addFile(u"./resources/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_btn.setIcon(icon3)
        self.horizontalLayout_2.addWidget(self.quit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delete_btn = QPushButton(self.gridLayoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u"./resources/delete_forever_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon4)
        self.horizontalLayout_4.addWidget(self.delete_btn)
        self.open_btn = QPushButton(self.gridLayoutWidget)
        self.open_btn.setObjectName(u"open_btn")
        icon5 = QIcon()
        icon5.addFile(u"./resources/folder_open_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_btn.setIcon(icon5)
        self.horizontalLayout_4.addWidget(self.open_btn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(False)
        self.listWidget.setStyleSheet(u"selection-color: rgb(255, 255, 255); "
                                      u"selection-background-color: rgb(76, 76, 76);")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.run_btn, self.settings_btn)
        QWidget.setTabOrder(self.settings_btn, self.create_btn)
        QWidget.setTabOrder(self.create_btn, self.quit_btn)
        QWidget.setTabOrder(self.quit_btn, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.delete_btn)
        QWidget.setTabOrder(self.delete_btn, self.open_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Linbox for 86Box", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"&Run", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"&Settings", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"&Create", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"&Delete", None))
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"&Open configuration folder...", None))
    # retranslateUi
