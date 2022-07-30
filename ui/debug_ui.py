# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        if not DebugWindow.objectName():
            DebugWindow.setObjectName(u"DebugWindow")
        DebugWindow.resize(400, 200)
        DebugWindow.setMinimumSize(QSize(400, 200))
        DebugWindow.setMaximumSize(QSize(400, 200))
        self.centralwidget = QWidget(DebugWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 104, 381, 86))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.open_note_debugger_button = QPushButton(self.gridLayoutWidget)
        self.open_note_debugger_button.setObjectName(u"open_note_debugger_button")

        self.gridLayout.addWidget(self.open_note_debugger_button, 0, 2, 1, 1)

        self.delete_settings_button = QPushButton(self.gridLayoutWidget)
        self.delete_settings_button.setObjectName(u"delete_settings_button")

        self.gridLayout.addWidget(self.delete_settings_button, 1, 1, 1, 1)

        self.recompile_uis_button = QPushButton(self.gridLayoutWidget)
        self.recompile_uis_button.setObjectName(u"recompile_uis_button")

        self.gridLayout.addWidget(self.recompile_uis_button, 1, 2, 1, 1)

        self.reset_settings_button = QPushButton(self.gridLayoutWidget)
        self.reset_settings_button.setObjectName(u"reset_settings_button")

        self.gridLayout.addWidget(self.reset_settings_button, 0, 1, 1, 1)

        self.open_settings_viewer_button = QPushButton(self.gridLayoutWidget)
        self.open_settings_viewer_button.setObjectName(u"open_settings_viewer_button")

        self.gridLayout.addWidget(self.open_settings_viewer_button, 2, 1, 1, 1)

        self.create_error_button = QPushButton(self.gridLayoutWidget)
        self.create_error_button.setObjectName(u"create_error_button")

        self.gridLayout.addWidget(self.create_error_button, 2, 2, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 193, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.instantly_open_settings_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.instantly_open_settings_checkbox.setObjectName(u"instantly_open_settings_checkbox")

        self.verticalLayout.addWidget(self.instantly_open_settings_checkbox)

        self.instantly_open_note_debugger_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.instantly_open_note_debugger_checkbox.setObjectName(u"instantly_open_note_debugger_checkbox")

        self.verticalLayout.addWidget(self.instantly_open_note_debugger_checkbox)

        DebugWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DebugWindow)

        QMetaObject.connectSlotsByName(DebugWindow)
    # setupUi

    def retranslateUi(self, DebugWindow):
        DebugWindow.setWindowTitle(QCoreApplication.translate("DebugWindow", u"Debug", None))
        self.open_note_debugger_button.setText(QCoreApplication.translate("DebugWindow", u"Open Note Debugger", None))
        self.delete_settings_button.setText(QCoreApplication.translate("DebugWindow", u"Delete Settings", None))
        self.recompile_uis_button.setText(QCoreApplication.translate("DebugWindow", u"Recompile UIs", None))
        self.reset_settings_button.setText(QCoreApplication.translate("DebugWindow", u"Reset Settings", None))
        self.open_settings_viewer_button.setText(QCoreApplication.translate("DebugWindow", u"Open Settings Viewer", None))
        self.create_error_button.setText(QCoreApplication.translate("DebugWindow", u"Create Error", None))
        self.instantly_open_settings_checkbox.setText(QCoreApplication.translate("DebugWindow", u"Instantly Open Settings", None))
        self.instantly_open_note_debugger_checkbox.setText(QCoreApplication.translate("DebugWindow", u"Instantly Open Note Debugger", None))
    # retranslateUi

