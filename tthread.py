

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread , pyqtSignal
import time



class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(515, 255)
        self.START1 = QtWidgets.QPushButton(Widget)
        self.START1.setGeometry(QtCore.QRect(40, 50, 75, 24))
        self.START1.setObjectName("START1")
        self.START2 = QtWidgets.QPushButton(Widget)
        self.START2.setGeometry(QtCore.QRect(40, 100, 75, 24))
        self.START2.setObjectName("START2")
        self.START3 = QtWidgets.QPushButton(Widget)
        self.START3.setGeometry(QtCore.QRect(40, 150, 75, 24))
        self.START3.setObjectName("START3")
        self.RESULT1 = QtWidgets.QTextBrowser(Widget)
        self.RESULT1.setGeometry(QtCore.QRect(160, 45, 101, 31))
        self.RESULT1.setObjectName("RESULT1")
        self.RESULT2 = QtWidgets.QTextBrowser(Widget)
        self.RESULT2.setGeometry(QtCore.QRect(160, 95, 101, 31))
        self.RESULT2.setObjectName("RESULT2")
        self.RESULT3 = QtWidgets.QTextBrowser(Widget)
        self.RESULT3.setGeometry(QtCore.QRect(160, 145, 101, 31))
        self.RESULT3.setObjectName("RESULT3")
        self.PROGRESS1 = QtWidgets.QProgressBar(Widget)
        self.PROGRESS1.setGeometry(QtCore.QRect(280, 50, 141, 23))
       
        self.PROGRESS1.setObjectName("PROGRESS1")
        self.PROGRESS2 = QtWidgets.QProgressBar(Widget)
        self.PROGRESS2.setGeometry(QtCore.QRect(280, 100, 141, 23))
        
        self.PROGRESS2.setObjectName("PROGRESS2")
        self.PROGRESS3 = QtWidgets.QProgressBar(Widget)
        self.PROGRESS3.setGeometry(QtCore.QRect(280, 150, 141, 23))
        
        self.PROGRESS3.setObjectName("PROGRESS3")
        self.OPS_ARE_DONE = QtWidgets.QLabel(Widget)
        self.OPS_ARE_DONE.setGeometry(QtCore.QRect(160, 210, 181, 16))
        self.OPS_ARE_DONE.setObjectName("OPS_ARE_DONE")
        self.OP1_done = QtWidgets.QLabel(Widget)
        self.OP1_done.setGeometry(QtCore.QRect(280, 55, 131, 16))
        self.OP1_done.setObjectName("OP1_done")
        self.OP2_done = QtWidgets.QLabel(Widget)
        self.OP2_done.setGeometry(QtCore.QRect(280, 105, 131, 16))
        self.OP2_done.setObjectName("OP2_done")
        self.OP3_done = QtWidgets.QLabel(Widget)
        self.OP3_done.setGeometry(QtCore.QRect(280, 155, 131, 16))
        self.OP3_done.setObjectName("OP3_done")



######visibility#######

        self.OP1_done.setVisible(False)
        self.OP2_done.setVisible(False)
        self.OP3_done.setVisible(False)
        self.OPS_ARE_DONE.setVisible(False)
######visibility#######






        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.START1.setText(_translate("Widget", "Start OP1"))
        self.START2.setText(_translate("Widget", "Start OP2"))
        self.START3.setText(_translate("Widget", "Start OP3"))
        self.OPS_ARE_DONE.setText(_translate("Widget", "ALL OPERATIONS ARE DONE!!!"))
        self.OP1_done.setText(_translate("Widget", "Operation1 is done !"))
        self.OP2_done.setText(_translate("Widget", "Operation 2 is done !"))
        self.OP3_done.setText(_translate("Widget", "Operation 3 is done !"))






    

######clicked-connection#######
        self.START1.clicked.connect(self.click1_start)

        self.START2.clicked.connect(self.click2_start)

        self.START3.clicked.connect(self.click3_start)
#########functions#############



    def click1_start(self):
        self.worker1 = Worker1()
        self.worker1.start()
        self.worker1.finished.connect(self.worker1_finish)
        self.worker1.update_progress1.connect(self.work1_update)
        
        
        

    def click2_start(self):
        self.worker2 =Worker2()
        self.worker2.start()
        self.worker2.finished.connect(self.worker2_finish)
        self.worker2.update_progress2.connect(self.work2_update)
        
        
        
    def click3_start(self):
        self.worker3 =Worker3()
        self.worker3.start()
        self.worker3.finished.connect(self.worker3_finish)
        self.worker3.update_progress3.connect(self.work3_update)
        
        
        

    def work1_update(self,value):

        self.PROGRESS1.setValue(value)

    def work2_update(self,value):

        self.PROGRESS2.setValue(value)


    def work3_update(self,value):

        self.PROGRESS3.setValue(value)






    def worker1_finish(self):

        self.PROGRESS1.setVisible(False)
        self.OP1_done.setVisible(True)




    def worker2_finish(self):

        self.PROGRESS2.setVisible(False)
        self.OP2_done.setVisible(True)

    def worker3_finish(self):
        self.PROGRESS3.setVisible(False)
        self.OP3_done.setVisible(True)


    def all_processes_are_done (self):

        if self.worker1.isFinished():
            if self.worker2.isFinished():
                if self.worker3.isFinished():

                    self.OPS_ARE_DONE.setVisible(True)




class Worker1(QThread):
    update_progress1 = pyqtSignal(int)

    def run(self):
        z = 0
        t = (100000*100001)/2
        for i in range(100000):
    
            z = z+i
            time.sleep(0.000001)
            self.update_progress1.emit(int((z/t)*100))
            
            

class Worker2(QThread):
    update_progress2 = pyqtSignal(int)

    def run(self):
        for i in range(100):
            time.sleep(0.03)

            self.update_progress2.emit(i)
        

class Worker3(QThread):
    update_progress3 = pyqtSignal(int)


    def run(self):
        for i in range(100):
            time.sleep(0.03)
            self.update_progress3.emit(i)
        







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())


z = 0
for i in range(100000000):
    
    z = z+i

print(z)