# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_note_checking.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_NoteDebugWindow(object):
    def setupUi(self, NoteDebugWindow):
        if not NoteDebugWindow.objectName():
            NoteDebugWindow.setObjectName(u"NoteDebugWindow")
        NoteDebugWindow.resize(400, 200)
        NoteDebugWindow.setMinimumSize(QSize(400, 200))
        NoteDebugWindow.setMaximumSize(QSize(400, 200))
        self.centralwidget = QWidget(NoteDebugWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(10, 170, 75, 24))
        self.note_debug_display = QTextBrowser(self.centralwidget)
        self.note_debug_display.setObjectName(u"note_debug_display")
        self.note_debug_display.setGeometry(QRect(10, 10, 381, 151))
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(316, 170, 75, 24))
        NoteDebugWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NoteDebugWindow)

        QMetaObject.connectSlotsByName(NoteDebugWindow)
    # setupUi

    def retranslateUi(self, NoteDebugWindow):
        NoteDebugWindow.setWindowTitle(QCoreApplication.translate("NoteDebugWindow", u"Note Debugging", None))
        self.clear_button.setText(QCoreApplication.translate("NoteDebugWindow", u"Clear", None))
        self.close_button.setText(QCoreApplication.translate("NoteDebugWindow", u"Close", None))
    # retranslateUi

