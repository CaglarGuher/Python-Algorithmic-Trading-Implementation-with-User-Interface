import pandas as pd
from Signal_Analysis import Signal_Analysis
from Get_coin_info import Get_info as GI
import time
import json



class Account(Signal_Analysis):

    def __init__(self , cash_balance ,coin_balance = {} , total_balance = 0   ):
        super().__init__(Signal_Analysis)
        self.total_balance = total_balance
        self.cash_balance = cash_balance
        self.coin_balance = coin_balance

        self.coin_balance = {
            "COIN_ACCOUNT":
            [
    
            {"coin" :"BTCUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"ETHUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"XRPUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"ADAUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"DOGEUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"MATICUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"DOTUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"DAIUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"SHIBUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            {"coin" :"BNBUSDT" ,"amount" : 0,"dolar_eq" : 0 ,"bought_unit_price" : 0},
            ]

}

    def Show_Balance(self):

        for data in self.coin_balance["COIN_ACCOUNT"]: 
            self.total_balance = self.total_balance + (data["amount"] * GI(data["coin"]).give_current_price()) 
        self.total_balance = self.total_balance + self.cash_balance

            
        print("ACCOUNT BALANCE  \n-------------------\nCASH == ",self.cash_balance )
        print("---------------")
        print("total balance is == ",self.total_balance)
        print("---------------")
        print("Coins")
        print(pd.DataFrame(self.coin_balance["COIN_ACCOUNT"]))

        self.total_balance = 0

            


    def Buy_Sell_coin(self):


        a = Signal_Analysis().suggest_random_coin()

        print(((self.cash_balance * 0.1)/GI(a).give_current_price()), "amount of " , a , " is bought ")

        for data in self.coin_balance["COIN_ACCOUNT"]:
            
            if data["coin"] == a :

                if data["amount"] == 0:

                    data["amount"] = data["amount"] +  (self.cash_balance * 0.1)/GI(a).give_current_price()
                    data["dolar_eq"] = self.cash_balance * 0.1
                    data["bought_unit_price"] = GI(a).give_current_price()

                    self.cash_balance = self.cash_balance -  self.cash_balance * 0.1

        



        
#result of the signal analysis will be bought with spesific amount


        
    
        
#if a coin is 1 percent up, sell it
#if a coin is down 0.5 percent, sell it
        
        
    def control_cash_amount(self):
        pass


        

       

        


    def Update_account(self):
        """
        refreshing the account every 1 sec
        
        """
        pass







'''
balance = {
            "COIN_ACCOUNT":
            [
    
            {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0},
            {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0},
            {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0},
            {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0},
            {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0},
            ]
}

print(pd.DataFrame(balance["COIN_ACCOUNT"]))


    

for data in balance["COIN_ACCOUNT"]:
    print(data , "\n----------------")
print("---------------------------------------")

time.sleep(2)


for data in balance["COIN_ACCOUNT"]:
    if data["coin"] == "XRPUSDT" :
        data["amount"] = data["amount"] + 25
    if data["coin"] == "BTCUSDT":
        data["amount"] = data["amount"] - 25

data = {"coin" : Signal_Analysis().suggest_random_coin(),"amount" : 100,"dolar_eq" : 0}

balance["COIN_ACCOUNT"].append(data)

for data in balance["COIN_ACCOUNT"]:
    print(data , "\n----------------")
print("---------------------------------------")

'''           

                
            
    



      

    

    
    
    







