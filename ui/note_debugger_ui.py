# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_debugger.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_NoteDebuggerWindow(object):
    def setupUi(self, NoteDebuggerWindow):
        if not NoteDebuggerWindow.objectName():
            NoteDebuggerWindow.setObjectName(u"NoteDebuggerWindow")
        NoteDebuggerWindow.resize(400, 200)
        NoteDebuggerWindow.setMinimumSize(QSize(400, 200))
        NoteDebuggerWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(NoteDebuggerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.note_debugger_layout = QVBoxLayout()
        self.note_debugger_layout.setObjectName(u"note_debugger_layout")
        self.note_debugger_display = QListWidget(self.centralwidget)
        self.note_debugger_display.setObjectName(u"note_debugger_display")

        self.note_debugger_layout.addWidget(self.note_debugger_display)


        self.verticalLayout_2.addLayout(self.note_debugger_layout)

        NoteDebuggerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NoteDebuggerWindow)

        QMetaObject.connectSlotsByName(NoteDebuggerWindow)
    # setupUi

    def retranslateUi(self, NoteDebuggerWindow):
        NoteDebuggerWindow.setWindowTitle(QCoreApplication.translate("NoteDebuggerWindow", u"Note Debugger", None))
    # retranslateUi

