


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(896, 600)
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(170, 100, 441, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 161, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Welcome to Testing"))
        self.pushButton.setText(_translate("Widget", "push button to start testing"))
        self.pushButton.clicked.connect(self.clicked__)

    def clicked__(self):
       
        self.label.setText("wow it works")
        self.label.setText("but why there")

class Ui_Widget1(object):
    def setupUi(self, Widget1):
        Widget1.setObjectName("Widget1")
        Widget1.resize(400, 600)
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
