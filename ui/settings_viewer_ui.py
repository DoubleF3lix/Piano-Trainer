# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SettingsViewer(object):
    def setupUi(self, SettingsViewer):
        if not SettingsViewer.objectName():
            SettingsViewer.setObjectName(u"SettingsViewer")
        SettingsViewer.resize(400, 500)
        self.centralwidget = QWidget(SettingsViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_display_layout = QVBoxLayout()
        self.settings_display_layout.setObjectName(u"settings_display_layout")
        self.settings_display = QTextEdit(self.centralwidget)
        self.settings_display.setObjectName(u"settings_display")
        self.settings_display.setLineWrapMode(QTextEdit.NoWrap)
        self.settings_display.setReadOnly(True)

        self.settings_display_layout.addWidget(self.settings_display)


        self.verticalLayout_2.addLayout(self.settings_display_layout)

        SettingsViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsViewer)

        QMetaObject.connectSlotsByName(SettingsViewer)
    # setupUi

    def retranslateUi(self, SettingsViewer):
        SettingsViewer.setWindowTitle(QCoreApplication.translate("SettingsViewer", u"Settings Viewer", None))
        self.settings_display.setHtml(QCoreApplication.translate("SettingsViewer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

