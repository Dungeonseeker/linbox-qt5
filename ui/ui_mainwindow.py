# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
                               QListWidget, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)
import ui.linbox_rc


class Ui_MainWindow(object):
    def setupui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        self.action_Run = QAction(MainWindow)
        self.action_Run.setObjectName(u"action_Run")
        icon = QIcon()
        icon.addFile(u":/resources/play_arrow_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.action_Run.setIcon(icon)
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
        icon1 = QIcon()
        icon1.addFile(u":/resources/settings_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.action_Settings.setIcon(icon1)
        self.action_Create = QAction(MainWindow)
        self.action_Create.setObjectName(u"action_Create")
        icon2 = QIcon()
        icon2.addFile(u":/resources/create_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.action_Create.setIcon(icon2)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        icon6 = QIcon()
        icon6.addFile(u":/resources/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.action_Quit.setIcon(icon6)
        self.action_About_Linbox = QAction(MainWindow)
        self.action_About_Linbox.setObjectName(u"action_About_Linbox")
        icon7 = QIcon()
        icon7.addFile(u":/resources/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.action_About_Linbox.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.centralwidget.setFont(font1)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 621, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delete_btn = QPushButton(self.gridLayoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/resources/delete_forever_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.delete_btn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.delete_btn)

        self.open_btn = QPushButton(self.gridLayoutWidget)
        self.open_btn.setObjectName(u"open_btn")
        icon4 = QIcon()
        icon4.addFile(u":/resources/folder_open_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.open_btn.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.open_btn)

        self.quit_btn = QPushButton(self.gridLayoutWidget)
        self.quit_btn.setObjectName(u"quit_btn")
        icon5 = QIcon()
        icon5.addFile(u":/resources/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.quit_btn.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.quit_btn)

        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_cmb = QComboBox(self.gridLayoutWidget)
        self.select_cmb.setObjectName(u"select_cmb")

        self.horizontalLayout_2.addWidget(self.select_cmb)

        self.run_btn = QPushButton(self.gridLayoutWidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setEnabled(False)
        self.run_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.run_btn)

        self.settings_btn = QPushButton(self.gridLayoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setEnabled(False)
        self.settings_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.settings_btn)

        self.create_btn = QPushButton(self.gridLayoutWidget)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.create_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(False)
        self.listWidget.setStyleSheet(u"color: rgb(255, 255, 255); selection-background-color:\n"
                                      "                                            rgb(76, 76, 76);\n"
                                      "                                        ")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.select_cmb, self.run_btn)
        QWidget.setTabOrder(self.run_btn, self.settings_btn)
        QWidget.setTabOrder(self.settings_btn, self.create_btn)
        QWidget.setTabOrder(self.create_btn, self.delete_btn)
        QWidget.setTabOrder(self.delete_btn, self.open_btn)
        QWidget.setTabOrder(self.open_btn, self.listWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.action_Run)
        self.menuFile.addAction(self.action_Settings)
        self.menuFile.addAction(self.action_Create)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuAbout.addAction(self.action_About_Linbox)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Linbox for 86Box - v1.2", None))
        self.action_Run.setText(QCoreApplication.translate("MainWindow", u"&Run...", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"&Settings...", None))
        self.action_Create.setText(QCoreApplication.translate("MainWindow", u"&Create...", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.action_About_Linbox.setText(QCoreApplication.translate("MainWindow", u"About Linbox", None))
        # if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected Virtual Machine", None))
        # endif // QT_CONFIG(tooltip)
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"&Delete", None))
        # if QT_CONFIG(tooltip)
        self.open_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Open Linbox configuration folder", None))
        # endif // QT_CONFIG(tooltip)
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"&Open configuration folder...", None))
        # if QT_CONFIG(tooltip)
        self.quit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Linbox for 86Box", None))
        # endif // QT_CONFIG(tooltip)
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        # if QT_CONFIG(tooltip)
        self.select_cmb.setToolTip(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p>Method to run the selected Virtual Machine with</p></body></html>",
                                                              None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.run_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Run selected Virtual Machine", None))
        # endif // QT_CONFIG(tooltip)
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"&Run", None))
        # if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Run selected Virtual Machine settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"&Settings", None))
        # if QT_CONFIG(tooltip)
        self.create_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Create a new Virtual Machine", None))
        # endif // QT_CONFIG(tooltip)
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"&Create", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi
