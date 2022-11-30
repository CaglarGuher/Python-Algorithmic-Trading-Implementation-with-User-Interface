# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extra.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget1(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(896, 600)
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(200, 90, 171, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 20, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 49, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "text1"))
        self.label_2.setText(_translate("Widget", "text2"))
        self.label_3.setText(_translate("Widget", "text3"))


