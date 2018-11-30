# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormAbout(object):
    def setupUi(self, FormAbout):
        FormAbout.setObjectName("FormAbout")
        FormAbout.resize(360, 180)
        FormAbout.setMinimumSize(QtCore.QSize(360, 180))
        FormAbout.setMaximumSize(QtCore.QSize(360, 180))
        self.gridLayout = QtWidgets.QGridLayout(FormAbout)
        self.gridLayout.setObjectName("gridLayout")
        self.btnClose = QtWidgets.QPushButton(FormAbout)
        self.btnClose.setAutoDefault(True)
        self.btnClose.setDefault(True)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.btnClose, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.textAbout = QtWidgets.QTextBrowser(FormAbout)
        self.textAbout.setObjectName("textAbout")
        self.gridLayout.addWidget(self.textAbout, 0, 0, 1, 2)

        self.retranslateUi(FormAbout)
        QtCore.QMetaObject.connectSlotsByName(FormAbout)

    def retranslateUi(self, FormAbout):
        _translate = QtCore.QCoreApplication.translate
        FormAbout.setWindowTitle(_translate("FormAbout", "CPU Notifier"))
        self.btnClose.setText(_translate("FormAbout", "Close"))
        self.textAbout.setHtml(_translate("FormAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">CPU Notifier</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool developed by <span style=\" font-weight:600;\">@ozcanyarimdunya</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source code is hosted at </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">https://github.com/ozcanyarimdunya/pyqt5-cpu</span></p></body></html>"))

