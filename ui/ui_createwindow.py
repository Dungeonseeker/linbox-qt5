# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

import ui.linbox_rc


class Ui_CreateWindow(object):
    def setupui(self, createwindow):
        if not createwindow.objectName():
            createwindow.setObjectName(u"createwindow")
        createwindow.setWindowModality(Qt.ApplicationModal)
        createwindow.setFixedSize(320, 160)
        self.verticalLayoutWidget = QWidget(createwindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 305, 145))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_entry = QLineEdit(self.verticalLayoutWidget)
        self.name_entry.setObjectName(u"name_entry")

        self.horizontalLayout_2.addWidget(self.name_entry)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_btn = QPushButton(self.verticalLayoutWidget)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u":/resources/ok_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ok_btn.setIcon(icon)
        self.ok_btn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(self.verticalLayoutWidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        icon1 = QIcon()
        icon1.addFile(u":/resources/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.cancel_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.name_entry, self.ok_btn)
        QWidget.setTabOrder(self.ok_btn, self.cancel_btn)

        self.retranslateUi(createwindow)

        QMetaObject.connectSlotsByName(createwindow)

    # setupUi

    def retranslateUi(self, createwindow):
        createwindow.setWindowTitle(QCoreApplication.translate("createwindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("createwindow", u"Virtual Machine Name:", None))
        self.label_2.setText(QCoreApplication.translate("createwindow", u"Slashes and whitespace are not allowed,\n"
                                                                        " they will be replaced with a hypen.", None))
        self.ok_btn.setText(QCoreApplication.translate("createwindow", u"&OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("createwindow", u"&Cancel", None))
    # retranslateUi
