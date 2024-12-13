# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QLabel, QProgressBar, QPushButton, QWidget)

class Ui_melodify(object):
    def setupUi(self, melodify):
        if not melodify.objectName():
            melodify.setObjectName(u"melodify")
        melodify.resize(492, 190)
        font = QFont()
        font.setFamilies([u"SF Pro"])
        melodify.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioCard))
        melodify.setWindowIcon(icon)
        melodify.setAutoFillBackground(False)
        melodify.setStyleSheet(u"")

        self.centralwidget = QWidget(melodify)
        self.centralwidget.setObjectName(u"centralwidget")

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(30, 20, 431, 31))
        font1 = QFont()
        font1.setFamilies([u"SF Pro"])
        font1.setPointSize(15)
        self.title_label.setFont(font1)

        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(220, 125, 51, 51))
        self.play_button.setAutoFillBackground(False)
        self.play_button.setStyleSheet("QPushButton {background-color: transparent; border: none;}")
        icon1 = QIcon()
        icon1.addFile(u"graphics/play_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(60, 60))

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(290, 130, 41, 41))
        self.next_button.setStyleSheet("QPushButton {background-color: transparent; border: none;}")
        icon2 = QIcon()
        icon2.addFile(u"graphics/next_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_button.setIcon(icon2)
        self.next_button.setIconSize(QSize(60, 60))

        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setGeometry(QRect(160, 130, 41, 41))
        self.prev_button.setStyleSheet("QPushButton {background-color: transparent; border: none;}")
        icon3 = QIcon()
        icon3.addFile(u"graphics/previous_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prev_button.setIcon(icon3)
        self.prev_button.setIconSize(QSize(60, 60))

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(30, 100, 431, 5))
        font2 = QFont()
        font2.setFamilies([u"SF Pro"])
        font2.setWeight(QFont.Light)
        font2.setStrikeOut(False)
        self.progress_bar.setFont(font2)
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border-radius: 5px;
                text-align: center;
                height: 10px; 
            }
            QProgressBar::chunk {
                background-color: white;
                border-radius: 5px;
            }
        """)

        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setOrientation(Qt.Orientation.Horizontal)
        self.progress_bar.setInvertedAppearance(False)

        self.file_button = QPushButton(self.centralwidget)
        self.file_button.setObjectName(u"file_button")
        self.file_button.setGeometry(QRect(430, 140, 31, 24))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.file_button.setIcon(icon4)
        melodify.setCentralWidget(self.centralwidget)

        self.retranslateUi(melodify)

        QMetaObject.connectSlotsByName(melodify)

    def retranslateUi(self, melodify):
        melodify.setWindowTitle(QCoreApplication.translate("melodify", u"Melodify", None))
        self.title_label.setText(QCoreApplication.translate("melodify", u"Play a song", None))
        self.play_button.setText("")
        self.next_button.setText("")
        self.prev_button.setText("")
        self.progress_bar.setFormat(QCoreApplication.translate("melodify", u"%p%", None))
        self.file_button.setText("")
