# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tt.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QThread
from Get_coin_info import Get_info as GI
from Account_Asset_Operation import Account 
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(160, 14, 400, 70))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)


        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        
        self.start_bot = QtWidgets.QPushButton(self.centralwidget)
        self.start_bot.setGeometry(QtCore.QRect(90, 90, 111, 24))


        ##edited3########################################################



        self.start_bot.clicked.connect(self.start_testing_loop)

        
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)

        self.start_bot.setFont(font)
        self.start_bot.setObjectName("start_bot")


        self.trading_started = QtWidgets.QLabel(self.centralwidget)
        self.trading_started.setGeometry(QtCore.QRect(90, 120, 121, 16))


        font = QtGui.QFont()
        font.setItalic(True)

        self.trading_started.setFont(font)
        self.trading_started.setObjectName("trading_started")


        self.account_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.account_display.setGeometry(QtCore.QRect(10, 230, 300, 221))
        self.account_display.setObjectName("account_display")


        self.Asset_order = QtWidgets.QLabel(self.centralwidget)
        self.Asset_order.setGeometry(QtCore.QRect(10, 150, 71, 16))


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)


        self.Asset_order.setFont(font)
        self.Asset_order.setObjectName("Asset_order")


        self.asset_order_show = QtWidgets.QTextBrowser(self.centralwidget)
        self.asset_order_show.setGeometry(QtCore.QRect(10, 170, 300, 31))
        self.asset_order_show.setObjectName("asset_order_show")


        self.account = QtWidgets.QLabel(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(10, 210, 61, 16))


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)


        self.account.setFont(font)
        self.account.setObjectName("account")


        self.total_balance = QtWidgets.QLabel(self.centralwidget)
        self.total_balance.setGeometry(QtCore.QRect(10, 460, 81, 16))


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)


        self.total_balance.setFont(font)
        self.total_balance.setObjectName("total_balance")


        self.cash_balance = QtWidgets.QLabel(self.centralwidget)
        self.cash_balance.setGeometry(QtCore.QRect(10, 520, 81, 16))


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)


        self.cash_balance.setFont(font)
        self.cash_balance.setObjectName("cash_balance")


        self.total_balance_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.total_balance_display.setGeometry(QtCore.QRect(10, 480, 300, 31))
        self.total_balance_display.setObjectName("total_balance_display")


        self.cash_balance_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.cash_balance_display.setGeometry(QtCore.QRect(10, 540, 300, 31))
        self.cash_balance_display.setObjectName("cash_balance_display")


        self.manual_coin_info = QtWidgets.QLabel(self.centralwidget)
        self.manual_coin_info.setGeometry(QtCore.QRect(390, 90, 211, 31))


        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)


        self.manual_coin_info.setFont(font)
        self.manual_coin_info.setObjectName("manual_coin_info")


        self.coin_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.coin_name_input.setGeometry(QtCore.QRect(430, 190, 121, 22))
        self.coin_name_input.setObjectName("coin_name_input")


        self.write_coin_name = QtWidgets.QLabel(self.centralwidget)
        self.write_coin_name.setGeometry(QtCore.QRect(440, 160, 111, 16))



        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)


        self.write_coin_name.setFont(font)
        self.write_coin_name.setObjectName("write_coin_name")


        self.show_price = QtWidgets.QPushButton(self.centralwidget)
        self.show_price.setGeometry(QtCore.QRect(430, 220, 121, 24))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 410, 110, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1min")
        self.comboBox.addItem("3min")
        self.comboBox.addItem("5min")
        self.comboBox.addItem("15min")
        self.comboBox.addItem("30min")
        self.comboBox.addItem("1h")
        self.comboBox.addItem("2h")
        self.comboBox.addItem("4h")
        self.comboBox.addItem("6h")
        self.comboBox.addItem("12h")
        self.comboBox.addItem("1d")
        self.comboBox.addItem("1w")
        self.comboBox.addItem("1m")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(368, 410, 100, 30))
        self.label.setFont(font)


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)


        self.show_price.setFont(font)
        self.show_price.setObjectName("show_price")


        ###adjusted##########################################################

        self.show_price.clicked.connect(self.give_coin_price)


        self.price_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.price_display.setGeometry(QtCore.QRect(360, 260, 256, 31))
        self.price_display.setObjectName("price_display")
        

        self.hist_data_vis = QtWidgets.QLabel(self.centralwidget)
        self.hist_data_vis.setGeometry(QtCore.QRect(370, 340, 241, 16))

        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)


        self.hist_data_vis.setFont(font)
        self.hist_data_vis.setObjectName("hist_data_vis")


        self.starting_date = QtWidgets.QLabel(self.centralwidget)
        self.starting_date.setGeometry(QtCore.QRect(370, 380, 101, 16))


        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)


        self.starting_date.setFont(font)
        self.starting_date.setObjectName("starting_date")


        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(480, 370, 110, 31))
        self.dateEdit.setObjectName("dateEdit")

########edited3#########################################################
        self.include_volume = QtWidgets.QCheckBox(self.centralwidget)
        self.include_volume.setGeometry(QtCore.QRect(370, 457, 121, 20))
        self.include_volume.setObjectName("include_volume")
        


        self.include_ma = QtWidgets.QCheckBox(self.centralwidget)
        self.include_ma.setGeometry(QtCore.QRect(370, 487, 91, 20))
        self.include_ma.setObjectName("include_ma")
        self.include_ma.clicked.connect(self.reveal_ma)
        

        self.ma1 = QtWidgets.QLabel(self.centralwidget)
        self.ma1.setGeometry(QtCore.QRect(370, 517, 49, 16))
        self.ma1.setObjectName("ma1")
        self.ma1.setVisible(False)


        self.ma2 = QtWidgets.QLabel(self.centralwidget)
        self.ma2.setGeometry(QtCore.QRect(370, 547, 49, 16))
        self.ma2.setObjectName("ma2")
        self.ma2.setVisible(False)


        self.ma1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ma1_input.setGeometry(QtCore.QRect(410, 517, 71, 22))
        self.ma1_input.setObjectName("ma1_input")
        self.ma1_input.setVisible(False)

        self.ma2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ma2_input.setGeometry(QtCore.QRect(410, 547, 71, 22))
        self.ma2_input.setObjectName("ma2_input")
        self.ma2_input.setVisible(False)

        ##edited2#######################################################
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 520, 161, 51))
        self.pushButton.clicked.connect(self.show_graphs)


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)


        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 22))
        self.menubar.setObjectName("menubar")


        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

################################Functions##########################################


    def give_coin_price(self):

        self.price_display.clear()

        self.price_display.append(str(GI(self.coin_name_input.text()).give_current_price()))


    

    def show_graphs(self):

        if self.include_ma.isChecked():

            
            result =GI(self.coin_name_input.text())
            result.hist_data_start_date(str(self.dateEdit.date().toPyDate()))
            result.set_ma1_value(int(self.ma1_input.text()))
            result.set_ma2_value(int(self.ma2_input.text()))
            result.set_price_interval(str(self.comboBox.currentText()))
            result.set_volume_visualization(self.include_volume.isChecked())

            return result.show_graph(self.include_ma.isChecked())

        else:



            result =GI(self.coin_name_input.text())
            result.hist_data_start_date(str(self.dateEdit.date().toPyDate()))
            result.set_price_interval(str(self.comboBox.currentText()))
            result.set_volume_visualization(self.include_volume.isChecked())

        
            return result.show_graph(self.include_ma.isChecked())
    def reveal_ma(self):
        
        self.include_ma.isChecked()
        self.ma1.setVisible(self.include_ma.isChecked())
        self.ma2.setVisible(self.include_ma.isChecked()) 
        self.ma1_input.setVisible(self.include_ma.isChecked())
        self.ma2_input.setVisible(self.include_ma.isChecked())

        a = False



        
    def start_testing_loop(self):
        acc = Account(10000)
        
        self.asset_order_show.append(str(acc.Buy_Sell_coin()))
        self.account_display.clear()
        
        self.total_balance_display.clear()
        acc.calculate_total_balance()
        self.total_balance_display.append(str(acc.calculate_total_balance()))
        self.cash_balance_display.clear()
        acc.show_cash_balance()
        self.cash_balance_display.append(str(acc.show_cash_balance()))
        
      
            

################################Functions#############################################

        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome to the Trading Bot Testing"))
        self.start_bot.setText(_translate("MainWindow", "Start Trading"))
        self.trading_started.setText(_translate("MainWindow", "Trading has started!"))
        self.Asset_order.setText(_translate("MainWindow", "Asset order :"))
        self.account.setText(_translate("MainWindow", "Account :"))
        self.total_balance.setText(_translate("MainWindow", "Total balance :"))
        self.cash_balance.setText(_translate("MainWindow", "Cash Balance :"))
        self.manual_coin_info.setText(_translate("MainWindow", "Manual Coin Information "))
        self.write_coin_name.setText(_translate("MainWindow", "Write a coin name:"))
        self.show_price.setText(_translate("MainWindow", "Show Price"))
        self.hist_data_vis.setText(_translate("MainWindow", "Historical Data Visualization"))
        self.starting_date.setText(_translate("MainWindow", "Starting Date :"))
        self.include_volume.setText(_translate("MainWindow", "include volume"))
        self.include_ma.setText(_translate("MainWindow", "include ma"))
        self.ma1.setText(_translate("MainWindow", "ma1 :"))
        self.ma2.setText(_translate("MainWindow", "ma2 :"))
        self.pushButton.setText(_translate("MainWindow", "Generate the Graph"))
        self.label.setText(_translate("MainWindow", "Price Interval : "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
