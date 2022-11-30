import threading
import time
from Account_Asset_Operation import Account

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(163, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.my_button = QtWidgets.QPushButton(self.centralwidget)
        self.my_button.setObjectName("my_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.my_button)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 163, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.my_button.setText(_translate("MainWindow", "Execute"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.valueChanged.connect(self.on_value_changed)
        self.my_button.clicked.connect(self.on_clicked)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        threading.Thread(target=self.my_function, daemon=True).start()

    @QtCore.pyqtSlot(int)
    def on_value_changed(self, value):
        self.textEdit.append("Value: {}".format(value))

    def my_function(self):
        for idx in range(10):
            self.valueChanged.emit(idx)
            print("Executing iteration " + str(idx) + " ...")
            time.sleep(1)  # replaces time-consuming task
        print("Finished!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())