# Form implementation generated from reading ui file 'c:\Users\tedla\prj\aademydatagui\ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 777)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 0, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.branch = QtWidgets.QComboBox(parent=self.centralwidget)
        self.branch.setMaximumSize(QtCore.QSize(300, 16777215))
        self.branch.setObjectName("branch")
        self.horizontalLayout.addWidget(self.branch)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 3)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.partype = QtWidgets.QComboBox(parent=self.centralwidget)
        self.partype.setObjectName("partype")
        self.gridLayout.addWidget(self.partype, 1, 1, 1, 5)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.series = QtWidgets.QComboBox(parent=self.centralwidget)
        self.series.setMaximumSize(QtCore.QSize(100, 16777215))
        self.series.setObjectName("series")
        self.gridLayout.addWidget(self.series, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.aa = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.aa.setMaximumSize(QtCore.QSize(100, 16777215))
        self.aa.setClearButtonEnabled(True)
        self.aa.setObjectName("aa")
        self.gridLayout.addWidget(self.aa, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 1)
        self.cafm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cafm.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cafm.setObjectName("cafm")
        self.gridLayout.addWidget(self.cafm, 2, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bnew_line = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bnew_line.setObjectName("bnew_line")
        self.horizontalLayout_2.addWidget(self.bnew_line)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tlines = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tlines.setObjectName("tlines")
        self.tlines.setColumnCount(5)
        self.tlines.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tlines.setHorizontalHeaderItem(4, item)
        self.tlines.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tlines)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bpost = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bpost.setObjectName("bpost")
        self.horizontalLayout_3.addWidget(self.bpost)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.results = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.results.setObjectName("results")
        self.verticalLayout.addWidget(self.results)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(parent=self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtGui.QAction(parent=MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtGui.QAction(parent=MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionexit)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.series.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.date, self.branch)
        MainWindow.setTabOrder(self.branch, self.partype)
        MainWindow.setTabOrder(self.partype, self.series)
        MainWindow.setTabOrder(self.series, self.aa)
        MainWindow.setTabOrder(self.aa, self.bnew_line)
        MainWindow.setTabOrder(self.bnew_line, self.tlines)
        MainWindow.setTabOrder(self.tlines, self.bpost)
        MainWindow.setTabOrder(self.bpost, self.results)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ημερομηνία"))
        self.label_5.setText(_translate("MainWindow", "Branch"))
        self.label_4.setText(_translate("MainWindow", "Τύπος"))
        self.label_2.setText(_translate("MainWindow", "Σειρά"))
        self.label_3.setText(_translate("MainWindow", "Παραστατικό"))
        self.label_6.setText(_translate("MainWindow", "ΑΦΜ ΠΕλάτη"))
        self.bnew_line.setText(_translate("MainWindow", "Νέα γραμμή"))
        item = self.tlines.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "αα"))
        item = self.tlines.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Κατηγορία"))
        item = self.tlines.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ε3"))
        item = self.tlines.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ΦΠΑ"))
        item = self.tlines.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ποσό"))
        self.bpost.setText(_translate("MainWindow", "Έκδοση"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
