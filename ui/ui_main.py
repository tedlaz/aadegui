# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 777)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.date = QDateEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date, 0, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label_5)

        self.branch = QComboBox(self.centralwidget)
        self.branch.setObjectName(u"branch")

        self.horizontalLayout.addWidget(self.branch)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.partype = QComboBox(self.centralwidget)
        self.partype.setObjectName(u"partype")

        self.gridLayout.addWidget(self.partype, 1, 1, 1, 5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.series = QComboBox(self.centralwidget)
        self.series.setObjectName(u"series")

        self.gridLayout.addWidget(self.series, 2, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.aa = QLineEdit(self.centralwidget)
        self.aa.setObjectName(u"aa")
        self.aa.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.aa, 2, 3, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 1)

        self.cafm = QLineEdit(self.centralwidget)
        self.cafm.setObjectName(u"cafm")

        self.gridLayout.addWidget(self.cafm, 2, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bnew_line = QPushButton(self.centralwidget)
        self.bnew_line.setObjectName(u"bnew_line")

        self.horizontalLayout_2.addWidget(self.bnew_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tlines = QTableWidget(self.centralwidget)
        if (self.tlines.columnCount() < 5):
            self.tlines.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tlines.setObjectName(u"tlines")
        self.tlines.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tlines)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bpost = QPushButton(self.centralwidget)
        self.bpost.setObjectName(u"bpost")

        self.horizontalLayout_3.addWidget(self.bpost)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.results = QTextEdit(self.centralwidget)
        self.results.setObjectName(u"results")

        self.verticalLayout.addWidget(self.results)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 25))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.date, self.branch)
        QWidget.setTabOrder(self.branch, self.partype)
        QWidget.setTabOrder(self.partype, self.series)
        QWidget.setTabOrder(self.series, self.aa)
        QWidget.setTabOrder(self.aa, self.bnew_line)
        QWidget.setTabOrder(self.bnew_line, self.tlines)
        QWidget.setTabOrder(self.tlines, self.bpost)
        QWidget.setTabOrder(self.bpost, self.results)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        self.series.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03cd\u03c0\u03bf\u03c2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u03a3\u03b5\u03b9\u03c1\u03ac", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03b1\u03c1\u03b1\u03c3\u03c4\u03b1\u03c4\u03b9\u03ba\u03cc", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03a6\u039c \u03a0\u0395\u03bb\u03ac\u03c4\u03b7", None))
        self.bnew_line.setText(QCoreApplication.translate("MainWindow", u"\u039d\u03ad\u03b1 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae", None))
        ___qtablewidgetitem = self.tlines.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u03b1\u03b1", None));
        ___qtablewidgetitem1 = self.tlines.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1", None));
        ___qtablewidgetitem2 = self.tlines.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u03953", None));
        ___qtablewidgetitem3 = self.tlines.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u03a6\u03a0\u0391", None));
        ___qtablewidgetitem4 = self.tlines.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03bf\u03c3\u03cc", None));
        self.bpost.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

