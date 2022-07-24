# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(597, 489)
        self.start_action = QAction(MainWindow)
        self.start_action.setObjectName(u"start_action")
        self.reset_action = QAction(MainWindow)
        self.reset_action.setObjectName(u"reset_action")
        self.stop_action = QAction(MainWindow)
        self.stop_action.setObjectName(u"stop_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_container = QLabel(self.centralwidget)
        self.image_container.setObjectName(u"image_container")
        self.image_container.setMinimumSize(QSize(400, 400))
        self.image_container.setMaximumSize(QSize(16777215, 16777215))
        self.image_container.setFrameShape(QFrame.Panel)
        self.image_container.setFrameShadow(QFrame.Sunken)
        self.image_container.setLineWidth(6)

        self.verticalLayout.addWidget(self.image_container)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tally_label = QLabel(self.centralwidget)
        self.tally_label.setObjectName(u"tally_label")
        font = QFont()
        font.setPointSize(12)
        self.tally_label.setFont(font)

        self.horizontalLayout.addWidget(self.tally_label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.skips_label = QLabel(self.centralwidget)
        self.skips_label.setObjectName(u"skips_label")
        self.skips_label.setFont(font)

        self.horizontalLayout.addWidget(self.skips_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_action.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.reset_action.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_action.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.image_container.setText("")
        self.tally_label.setText(QCoreApplication.translate("MainWindow", u"0/0 Correct", None))
        self.skips_label.setText(QCoreApplication.translate("MainWindow", u"0 Skips", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

