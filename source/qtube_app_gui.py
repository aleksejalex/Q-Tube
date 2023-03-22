# -*- coding: utf-8 -*-
from typing import Optional

import PySide6
################################################################################
## Form generated from reading UI file 'q-tube_app_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
                               QMenu, QMenuBar, QPlainTextEdit, QPushButton,
                               QSizePolicy, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., flags: PySide6.QtCore.Qt.WindowType = ...):
        super().__init__(parent, flags)
        self.actionNew = QAction(QMainWindow)
        self.actionRedownload = QAction(QMainWindow)
        self.actionQuit = QAction(QMainWindow)
        self.centralwidget = QWidget(QMainWindow)
        self.pushButton_download = QPushButton(self.centralwidget)


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 530)
        #self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        #self.actionRedownload = QAction(MainWindow)
        self.actionRedownload.setObjectName(u"actionRedownload")
        #self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionInfo_about_Q_Tube = QAction(MainWindow)
        self.actionInfo_about_Q_Tube.setObjectName(u"actionInfo_about_Q_Tube")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_download = QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.clicked.connect(self.the_buton_was_clickedd)

        self.verticalLayout.addWidget(self.pushButton_download)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.verticalLayout.addWidget(self.pushButton_reset)

        self.pushButton_quit = QPushButton(self.centralwidget)
        self.pushButton_quit.clicked.connect(self.the_buton_was_clickedd())
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.verticalLayout.addWidget(self.pushButton_quit)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionRedownload)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionInfo_about_Q_Tube)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionRedownload.setText(QCoreApplication.translate("MainWindow", u"Redownload", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionInfo_about_Q_Tube.setText(QCoreApplication.translate("MainWindow", u"Info about Q-Tube", None))
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi


    def the_buton_was_clickedd(self):
        print("boton clicked (inside gui class)")