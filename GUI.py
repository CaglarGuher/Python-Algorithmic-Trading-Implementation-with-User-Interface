
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QThread ,  pyqtSignal
from Get_coin_info import Get_info as GI
from Account_Asset_Operation import Account 
from Df_adjusting_process import DataFrameModel
from Signal_Analysis import Signal_Analysis as SA
import time
import pandas as pd



class ENTRY(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(684, 205)
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 65, 471, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 115, 471, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 211, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 391, 20))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Your Api KEY:"))
        self.label_2.setText(_translate("Widget", "Your Api SECRET:"))
        self.pushButton.setText(_translate("Widget", "SUBMIT "))
        self.label_3.setText(_translate("Widget", "REQUIRED INFORMATIONS FOR THE ALGORTIHM"))
        self.pushButton.clicked.connect(self.go_to_main)

    def go_to_main(self):

        self.MainWindow1 = QtWidgets.QMainWindow()
        self.uu1 = MAIN()
        self.uu1.setupUi(self.MainWindow1)
        
        self.MainWindow1.show()
        Widget.close()
        




##############MAIN GUI CLASS##################
class MAIN(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 630)


###MAIN FRAME##
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

###MAIN FRAME##



####WELCOME TEXT######

        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(160, 14, 400, 70))

        font = QtGui.QFont()
        font.setPixelSize(18)
        


        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")

####WELCOME TEXT######


####STARTING BOT BUTTON######
        
        self.start_bot = QtWidgets.QPushButton(self.centralwidget)
        self.start_bot.setGeometry(QtCore.QRect(90, 90, 130, 24))
        

        




        
        font = QtGui.QFont()
        font.setPixelSize(13)
        

        self.start_bot.setFont(font)
        self.start_bot.setObjectName("start_bot")


####STARTING BOT BUTTON######


####STOP BOT BUTTON######

        self.stop_bot = QtWidgets.QPushButton(self.centralwidget)

        self.stop_bot.setGeometry(QtCore.QRect(90, 580, 130, 24))

        
        
        font = QtGui.QFont()
        font.setPixelSize(13)
        

        self.stop_bot.setFont(font)
        self.stop_bot.setObjectName("stop_bot")
        
####STOP BOT BUTTON######


####TRADING STARTED TEXT ######


        self.trading_started = QtWidgets.QLabel(self.centralwidget)
        self.trading_started.setGeometry(QtCore.QRect(90, 120, 121, 16))
        self.trading_started.setVisible(False)


        font = QtGui.QFont()
        

        self.trading_started.setFont(font)
        self.trading_started.setObjectName("trading_started")

####TRADING STARTED TEXT ######


####TRADING ENDED TEXT ######

        self.trading_ended = QtWidgets.QLabel(self.centralwidget)
        self.trading_ended.setGeometry(QtCore.QRect(210, 585, 121, 16))
        self.trading_ended.setVisible(False)
        


        font = QtGui.QFont()
        

        self.trading_ended.setFont(font)
        self.trading_ended.setObjectName("trading_ended")

####TRADING ENDED TEXT ######
  

####ACCOUNT DISPLAY TABLE

        self.account_display = QtWidgets.QTableView(self.centralwidget)
        self.account_display.setGeometry(QtCore.QRect(10, 230, 300, 221))
        self.account_display.setObjectName("account_display")


####ACCOUNT DISPLAY TABLE


###ASSET ORDER TEXT LABEL#######

        self.Asset_order = QtWidgets.QLabel(self.centralwidget)
        self.Asset_order.setGeometry(QtCore.QRect(10, 150, 71, 16))

        font = QtGui.QFont()
        font.setPixelSize(13)
        

        self.Asset_order.setFont(font)
        self.Asset_order.setObjectName("Asset_order")

###ASSET ORDER TEXT LABEL#######




###ASSET ORDER DISPLAY LABEL#######

        self.asset_order_show = QtWidgets.QTextBrowser(self.centralwidget)
        self.asset_order_show.setGeometry(QtCore.QRect(10, 170, 300, 31))
        self.asset_order_show.setObjectName("asset_order_show")

###ASSET ORDER DISPLAY LABEL#######


###ACCOUNT TEXT LABEL###


        self.account = QtWidgets.QLabel(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(10, 210, 61, 16))


        font = QtGui.QFont()
        font.setPixelSize(13)
        


        self.account.setFont(font)
        self.account.setObjectName("account")

###ACCOUNT TEXT LABEL###



###TOTAL BALANCE TEXT LABEL####

        self.total_balance = QtWidgets.QLabel(self.centralwidget)
        self.total_balance.setGeometry(QtCore.QRect(10, 460, 132, 16))

        font = QtGui.QFont()
        font.setPixelSize(13)
        

        self.total_balance.setFont(font)
        self.total_balance.setObjectName("total_balance")

###TOTAL BALANCE TEXT LABEL####



####CASH BALANCE TEXT LABEL####

        self.cash_balance = QtWidgets.QLabel(self.centralwidget)
        self.cash_balance.setGeometry(QtCore.QRect(10, 520, 81, 16))

        font = QtGui.QFont()
        font.setPixelSize(13)
        

        self.cash_balance.setFont(font)
        self.cash_balance.setObjectName("cash_balance")

####CASH BALANCE TEXT LABEL####



####TOTAL BALANCE DISPLAY####

        self.total_balance_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.total_balance_display.setGeometry(QtCore.QRect(10, 480, 300, 31))
        self.total_balance_display.setObjectName("total_balance_display")

####TOTAL BALANCE DISPLAY####



####CASH BALANCE DISPLAY####

        self.cash_balance_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.cash_balance_display.setGeometry(QtCore.QRect(10, 540, 300, 31))
        self.cash_balance_display.setObjectName("cash_balance_display")

####CASH BALANCE DISPLAY####



###MANUAL COIN INFO TEXT LABEL###
        self.manual_coin_info = QtWidgets.QLabel(self.centralwidget)
        self.manual_coin_info.setGeometry(QtCore.QRect(390, 90, 211, 31))

        font = QtGui.QFont()
        font.setPixelSize(17)
        

        self.manual_coin_info.setFont(font)
        self.manual_coin_info.setObjectName("manual_coin_info")

###MANUAL COIN INFO TEXT LABEL###



####COIN NAME INPUT####

        self.coin_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.coin_name_input.setGeometry(QtCore.QRect(430, 190, 121, 22))
        self.coin_name_input.setObjectName("coin_name_input")

####COIN NAME INPUT####



###COIN NAME TEXT LABEL###

        self.write_coin_name = QtWidgets.QLabel(self.centralwidget)
        self.write_coin_name.setGeometry(QtCore.QRect(440, 160, 111, 16))

        font = QtGui.QFont()
        font.setPixelSize(12)
        

        self.write_coin_name.setFont(font)
        self.write_coin_name.setObjectName("write_coin_name")

###COIN NAME TEXT LABEL###



###SHOW PRICE BUTTON###

        self.show_price = QtWidgets.QPushButton(self.centralwidget)
        self.show_price.setGeometry(QtCore.QRect(430, 220, 121, 24))
        self.show_price.setFont(font)
        self.show_price.setObjectName("show_price")

###SHOW PRICE BUTTON###




###INTERVAL SELECTION COMBOBOX####

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

###INTERVAL SELECTION COMBOBOX####

        

###PRICE INTERVAL TEXT LABEL###

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(368, 410, 100, 30))
        self.label.setFont(font)

        font = QtGui.QFont()
        font.setPixelSize(13)
        

###PRICE INTERVAL TEXT LABEL###




        
#############################################################

        

###PRICE DISPLAY####

        self.price_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.price_display.setGeometry(QtCore.QRect(360, 260, 256, 31))
        self.price_display.setObjectName("price_display")

###PRICE DISPLAY####


### HISTORICAL DATA TEXT LABEL###
        
        self.hist_data_vis = QtWidgets.QLabel(self.centralwidget)
        self.hist_data_vis.setGeometry(QtCore.QRect(370, 340, 241, 16))
        
        font = QtGui.QFont()
        font.setPixelSize(17)
        

        self.hist_data_vis.setFont(font)
        self.hist_data_vis.setObjectName("hist_data_vis")

### HISTORICAL DATA TEXT LABEL###



###STARTING DATE TEXT LABEL###

        self.starting_date = QtWidgets.QLabel(self.centralwidget)
        self.starting_date.setGeometry(QtCore.QRect(370, 380, 101, 16))

        font = QtGui.QFont()
        font.setPixelSize(14)
        

        self.starting_date.setFont(font)
        self.starting_date.setObjectName("starting_date")

###STARTING DATE TEXT LABEL###




####DATE INPUT ####

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(480, 370, 110, 31))
        self.dateEdit.setObjectName("dateEdit")

####DATE INPUT ####



###INCLUDE VOLUME CHECKBOX###

        self.include_volume = QtWidgets.QCheckBox(self.centralwidget)
        self.include_volume.setGeometry(QtCore.QRect(370, 457, 121, 20))
        self.include_volume.setObjectName("include_volume")
        
###INCLUDE VOLUME CHECKBOX###



###INCLUDE MA CHECKBOX###

        self.include_ma = QtWidgets.QCheckBox(self.centralwidget)
        self.include_ma.setGeometry(QtCore.QRect(370, 487, 91, 20))
        self.include_ma.setObjectName("include_ma")
        
        
###INCLUDE MA CHECKBOX###



###MA1 TEXT LABEL

        self.ma1 = QtWidgets.QLabel(self.centralwidget)
        self.ma1.setGeometry(QtCore.QRect(370, 517, 49, 16))
        self.ma1.setObjectName("ma1")
        self.ma1.setVisible(False)

###MA1 TEXT LABEL



###MA2 TEXT LABEL###

        self.ma2 = QtWidgets.QLabel(self.centralwidget)
        self.ma2.setGeometry(QtCore.QRect(370, 547, 49, 16))
        self.ma2.setObjectName("ma2")
        self.ma2.setVisible(False)

###MA2 TEXT LABEL###



###MA1 INPUT ###

        self.ma1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ma1_input.setGeometry(QtCore.QRect(410, 517, 71, 22))
        self.ma1_input.setObjectName("ma1_input")
        self.ma1_input.setVisible(False)

###MA1 INPUT ###



###MA2 INPUT###

        self.ma2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ma2_input.setGeometry(QtCore.QRect(410, 547, 71, 22))
        self.ma2_input.setObjectName("ma2_input")
        self.ma2_input.setVisible(False)

###MA2 INPUT


###SHOW GRAPH BUTTON###

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 520, 161, 51))
        

        font = QtGui.QFont()
        font.setPixelSize(15)
        

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

###SHOW GRAPH BUTTON###



###BUTTON CONNECTIONS###

        self.start_bot.clicked.connect(self.start_trading)
        self.stop_bot.clicked.connect(self.end_trading)
        self.show_price.clicked.connect(self.give_coin_price)
        self.include_ma.clicked.connect(self.reveal_ma)
        self.pushButton.clicked.connect(self.show_graphs)

###BUTTON CONNECTIONS###


##### MENU ADJUSTING SETTINGS ####

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome to the Trading Bot Testing"))
        self.start_bot.setText(_translate("MainWindow", "Start Balance Display"))
        self.trading_started.setText(_translate("MainWindow", "Trading has started!"))
        self.Asset_order.setText(_translate("MainWindow", "Asset order :"))
        self.account.setText(_translate("MainWindow", "Account :"))
        self.total_balance.setText(_translate("MainWindow", "Total asset balance :"))
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
        self.stop_bot.setText(_translate("MainWindow", "Stop Balance Display"))
        self.trading_ended.setText(_translate("MainWindow", "Trading has ended!"))

##### MENU ADJUSTING SETTINGS ####







###FUNCTIONS###

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



    def start_trading(self):
        self.trading_ended.setVisible(False)
        self.worker1 = Coin_Info_Response()
        self.thread = QThread()
        self.thread.start()
        self.worker1.moveToThread(self.thread)
        self.thread.started.connect(self.worker1.run)
        self.trading_started.setVisible(True)
        self.worker1.Cash_balance_signal.connect(self.emit_cash_balance)
        self.worker1.total_balance_signal.connect(self.emit_total_balance)
        self.worker1.Coin_bought_signal.connect(self.emit_coin_bought)  
        self.worker1.dataframe_signal.connect(self.emit_and_turn_into_df) 



    def end_trading(self):
        self.trading_started.setVisible(False)
        self.worker1.stop()
        self.thread.terminate()
        self.asset_order_show.clear()
        self.trading_ended.setVisible(True)



        
    def emit_cash_balance(self,value):
        self.cash_balance_display.setText(str(value))



    def emit_total_balance(self,value):
        self.total_balance_display.setText(str(value))



    def emit_coin_bought(self,value):
        self.asset_order_show.setText(str(value))



    def emit_and_turn_into_df(self,value):
        self.datframe = pd.DataFrame(value)
        self.model = DataFrameModel(self.datframe)
        self.account_display.setModel(self.model)



###FUNCTIONS###



       
##############MAIN GUI CLASS##################




###QTHREAD CLASS##############################

class Coin_Info_Response(QThread):

    
    total_balance_signal = pyqtSignal(str)
    Coin_bought_signal = pyqtSignal(str)
    Cash_balance_signal = pyqtSignal(float)
    dataframe_signal = pyqtSignal(list)



    def run(self):
        self.start_trading = True
        
        while self.start_trading:
            self.account = Account()
            self.total_balance_signal.emit(self.account.show_total_balance())
            self.Coin_bought_signal.emit("testing, no coin will be bought")
            self.Cash_balance_signal.emit(self.account.show_cash_balance())
            self.dataframe_signal.emit(self.account.give_coin_balance())
            time.sleep(0.1)



    def stop(self):
        self.start_trading = False

###QTHREAD CLASS##############################
        


####SYS####    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = ENTRY()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())



####SYS####    







