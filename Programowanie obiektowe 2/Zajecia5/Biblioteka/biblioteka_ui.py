# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'biblioteka.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 611, 311))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.filterCombo = QComboBox(self.widget)
        self.filterCombo.addItem("")
        self.filterCombo.addItem("")
        self.filterCombo.addItem("")
        self.filterCombo.setObjectName(u"filterCombo")

        self.verticalLayout.addWidget(self.filterCombo)

        self.bookTable = QTableView(self.widget)
        self.bookTable.setObjectName(u"bookTable")

        self.verticalLayout.addWidget(self.bookTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.borrowButton = QPushButton(self.widget)
        self.borrowButton.setObjectName(u"borrowButton")

        self.horizontalLayout.addWidget(self.borrowButton)

        self.returnButton = QPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 636, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filterCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Wszystkie", None))
        self.filterCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Dost\u0119pne", None))
        self.filterCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Wypo\u017cyczone", None))

        self.borrowButton.setText(QCoreApplication.translate("MainWindow", u"Wypo\u017cycz", None))
        self.returnButton.setText(QCoreApplication.translate("MainWindow", u"Zwr\u00f3\u0107", None))
    # retranslateUi

