

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal , QThread

from PyQt5.QtWidgets import QInputDialog, QFileDialog ,QApplication , QDialog 

from Df_adjusting_process import DataFrameModel

class Entry(object):

       
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 184)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(280, 100, 22, 22))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(20, 100, 261, 22))
        self.lineEdit1.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 75, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Choose Csv File"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.toolButton.clicked.connect(self.btn_clk)
        self.pushButton.clicked.connect(self.move_to_result)


    def btn_clk(self):
           
        self.filename = QFileDialog.getOpenFileName()
        self.lineEdit1.setText(self.filename[0])
        
    def give_filename(self):

        return self.filename[0]

        
    def give_line_path(self):

        return self.lineEdit1.text()


    def move_to_result(self):

        
        self.MainWindow1 = QtWidgets.QMainWindow()
        self.ui = DOC_SHOW_DATAFRAME(self.filename[0])
        self.ui.setupUi(self.MainWindow1)
        self.MainWindow1.show()
         
        MainWindow.close()

    



        
class Show_DataFrame(object):

    def __init__(self, df_path = str):


        self.df = df_path

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
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



        dataframe = pd.read_csv(self.df)
        model = DataFrameModel(dataframe)
        self.tableView.setModel(model)



class DOC_SHOW_DATAFRAME(object):

    def __init__(self,df_path):


        self.df_path = df_path



    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(255, 169)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 201, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 100, 201, 24))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)


        self.pushButton.clicked.connect(self.show_dataframe)


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "Show Dataframe"))
        self.pushButton_2.setText(_translate("Widget", "Document The Data"))


    def show_dataframe(self):

        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = Show_DataFrame(self.df_path)
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()
         
        MainWindow.close()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Entry()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = DOC_SHOW_DATAFRAME()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())