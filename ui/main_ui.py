# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 489)
        self.start_action = QAction(MainWindow)
        self.start_action.setObjectName("start_action")
        self.reset_action = QAction(MainWindow)
        self.reset_action.setObjectName("reset_action")
        self.stop_action = QAction(MainWindow)
        self.stop_action.setObjectName("stop_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_container = QLabel(self.centralwidget)
        self.image_container.setObjectName("image_container")
        self.image_container.setMinimumSize(QSize(400, 400))
        self.image_container.setMaximumSize(QSize(16777215, 16777215))
        self.image_container.setFrameShape(QFrame.Panel)
        self.image_container.setFrameShadow(QFrame.Sunken)
        self.image_container.setLineWidth(6)

        self.verticalLayout.addWidget(self.image_container)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tally_label = QLabel(self.centralwidget)
        self.tally_label.setObjectName("tally_label")
        font = QFont()
        font.setPointSize(12)
        self.tally_label.setFont(font)

        self.horizontalLayout.addWidget(self.tally_label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.skips_label = QLabel(self.centralwidget)
        self.skips_label.setObjectName("skips_label")
        self.skips_label.setFont(font)

        self.horizontalLayout.addWidget(self.skips_label)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.clef_label = QLabel(self.centralwidget)
        self.clef_label.setObjectName("clef_label")
        self.clef_label.setFont(font)

        self.horizontalLayout.addWidget(self.clef_label)

        self.clef_selection = QComboBox(self.centralwidget)
        self.clef_selection.addItem("")
        self.clef_selection.addItem("")
        self.clef_selection.addItem("")
        self.clef_selection.setObjectName("clef_selection")
        self.clef_selection.setFont(font)

        self.horizontalLayout.addWidget(self.clef_selection)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName("settings_button")
        self.settings_button.setFont(font)

        self.horizontalLayout.addWidget(self.settings_button)

        self.skip_button = QPushButton(self.centralwidget)
        self.skip_button.setObjectName("skip_button")
        self.skip_button.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.skip_button.setFont(font1)
        self.skip_button.setAutoFillBackground(False)
        self.skip_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.skip_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 597, 22))
        self.menuStart = QMenu(self.menuBar)
        self.menuStart.setObjectName("menuStart")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuStart.menuAction())
        self.menuStart.addAction(self.start_action)
        self.menuStart.addAction(self.stop_action)
        self.menuStart.addAction(self.reset_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.start_action.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )
        self.reset_action.setText(
            QCoreApplication.translate("MainWindow", "Reset", None)
        )
        self.stop_action.setText(QCoreApplication.translate("MainWindow", "Stop", None))
        self.image_container.setText("")
        self.tally_label.setText(
            QCoreApplication.translate("MainWindow", "0/0 Correct", None)
        )
        self.skips_label.setText(
            QCoreApplication.translate("MainWindow", "0 Skips", None)
        )
        self.clef_label.setText(QCoreApplication.translate("MainWindow", "Clef:", None))
        self.clef_selection.setItemText(
            0, QCoreApplication.translate("MainWindow", "Bass", None)
        )
        self.clef_selection.setItemText(
            1, QCoreApplication.translate("MainWindow", "Treble", None)
        )
        self.clef_selection.setItemText(
            2, QCoreApplication.translate("MainWindow", "Random", None)
        )

        self.settings_button.setText(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        self.skip_button.setText(QCoreApplication.translate("MainWindow", "Skip", None))
        # if QT_CONFIG(shortcut)
        self.skip_button.setShortcut(
            QCoreApplication.translate("MainWindow", "S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.menuStart.setTitle(QCoreApplication.translate("MainWindow", "Menu", None))

    # retranslateUi
