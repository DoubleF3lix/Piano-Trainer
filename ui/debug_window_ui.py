# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_window.ui'
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
    QPushButton, QSizePolicy, QWidget)

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
        self.gridLayoutWidget.setGeometry(QRect(11, 100, 381, 86))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.open_note_debugging_button = QPushButton(self.gridLayoutWidget)
        self.open_note_debugging_button.setObjectName(u"open_note_debugging_button")

        self.gridLayout.addWidget(self.open_note_debugging_button, 0, 2, 1, 1)

        self.delete_settings_button = QPushButton(self.gridLayoutWidget)
        self.delete_settings_button.setObjectName(u"delete_settings_button")

        self.gridLayout.addWidget(self.delete_settings_button, 1, 1, 1, 1)

        self.recompile_uis_button = QPushButton(self.gridLayoutWidget)
        self.recompile_uis_button.setObjectName(u"recompile_uis_button")

        self.gridLayout.addWidget(self.recompile_uis_button, 1, 2, 1, 1)

        self.reset_settings_button = QPushButton(self.gridLayoutWidget)
        self.reset_settings_button.setObjectName(u"reset_settings_button")

        self.gridLayout.addWidget(self.reset_settings_button, 0, 1, 1, 1)

        self.open_log_button = QPushButton(self.gridLayoutWidget)
        self.open_log_button.setObjectName(u"open_log_button")

        self.gridLayout.addWidget(self.open_log_button, 2, 2, 1, 1)

        self.fetch_settings_button = QPushButton(self.gridLayoutWidget)
        self.fetch_settings_button.setObjectName(u"fetch_settings_button")

        self.gridLayout.addWidget(self.fetch_settings_button, 2, 1, 1, 1)

        self.instantly_open_settings_checkbox = QCheckBox(self.centralwidget)
        self.instantly_open_settings_checkbox.setObjectName(u"instantly_open_settings_checkbox")
        self.instantly_open_settings_checkbox.setGeometry(QRect(10, 10, 141, 20))
        self.is_running_python_checkbox = QCheckBox(self.centralwidget)
        self.is_running_python_checkbox.setObjectName(u"is_running_python_checkbox")
        self.is_running_python_checkbox.setGeometry(QRect(10, 36, 120, 20))
        self.open_dialog_on_error_checkbox = QCheckBox(self.centralwidget)
        self.open_dialog_on_error_checkbox.setObjectName(u"open_dialog_on_error_checkbox")
        self.open_dialog_on_error_checkbox.setGeometry(QRect(10, 62, 136, 20))
        self.save_and_quit_button = QPushButton(self.centralwidget)
        self.save_and_quit_button.setObjectName(u"save_and_quit_button")
        self.save_and_quit_button.setGeometry(QRect(294, 10, 91, 24))
        DebugWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DebugWindow)

        QMetaObject.connectSlotsByName(DebugWindow)
    # setupUi

    def retranslateUi(self, DebugWindow):
        DebugWindow.setWindowTitle(QCoreApplication.translate("DebugWindow", u"Debug", None))
        self.open_note_debugging_button.setText(QCoreApplication.translate("DebugWindow", u"Open Note Debugging", None))
        self.delete_settings_button.setText(QCoreApplication.translate("DebugWindow", u"Delete Settings", None))
        self.recompile_uis_button.setText(QCoreApplication.translate("DebugWindow", u"Recompile UIs", None))
        self.reset_settings_button.setText(QCoreApplication.translate("DebugWindow", u"Reset Settings", None))
        self.open_log_button.setText(QCoreApplication.translate("DebugWindow", u"Open Log", None))
        self.fetch_settings_button.setText(QCoreApplication.translate("DebugWindow", u"Fetch Settings", None))
        self.instantly_open_settings_checkbox.setText(QCoreApplication.translate("DebugWindow", u"Instantly Open Settings", None))
        self.is_running_python_checkbox.setText(QCoreApplication.translate("DebugWindow", u"Is Running Python", None))
        self.open_dialog_on_error_checkbox.setText(QCoreApplication.translate("DebugWindow", u"Open Dialog On Error", None))
        self.save_and_quit_button.setText(QCoreApplication.translate("DebugWindow", u"Save and Quit", None))
    # retranslateUi

