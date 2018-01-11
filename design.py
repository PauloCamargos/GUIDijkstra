# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(378, 412)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblOrigin = QtGui.QLabel(self.centralwidget)
        self.lblOrigin.setObjectName(_fromUtf8("lblOrigin"))
        self.horizontalLayout.addWidget(self.lblOrigin)
        self.cboxOrigin = QtGui.QComboBox(self.centralwidget)
        self.cboxOrigin.setObjectName(_fromUtf8("cboxOrigin"))
        self.horizontalLayout.addWidget(self.cboxOrigin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblDestiny = QtGui.QLabel(self.centralwidget)
        self.lblDestiny.setObjectName(_fromUtf8("lblDestiny"))
        self.horizontalLayout_3.addWidget(self.lblDestiny)
        self.cboxDestiny = QtGui.QComboBox(self.centralwidget)
        self.cboxDestiny.setObjectName(_fromUtf8("cboxDestiny"))
        self.horizontalLayout_3.addWidget(self.cboxDestiny)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.verticalLayout_2.addWidget(self.btnSearch)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtMessage = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtMessage.setReadOnly(True)
        self.txtMessage.setPlainText(_fromUtf8(""))
        self.txtMessage.setOverwriteMode(True)
        self.txtMessage.setBackgroundVisible(False)
        self.txtMessage.setObjectName(_fromUtf8("txtMessage"))
        self.verticalLayout.addWidget(self.txtMessage)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dijkstra Search", None))
        self.lblOrigin.setText(_translate("MainWindow", "Origin", None))
        self.lblDestiny.setText(_translate("MainWindow", "Destiny", None))
        self.btnSearch.setText(_translate("MainWindow", "Search", None))

from PyQt4 import QtWebKit
