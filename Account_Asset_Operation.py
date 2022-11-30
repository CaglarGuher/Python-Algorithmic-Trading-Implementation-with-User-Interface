import pandas as pd
from Signal_Analysis import Signal_Analysis
from Get_coin_info import Get_info as GI
import time
import json



class Account(Signal_Analysis):

    def __init__(self , cash_balance ,coin_balance = {}  ):
        super().__init__(Signal_Analysis)
     
        self.cash_balance = cash_balance
        self.coin_balance = coin_balance

        self.coin_balance = {
            "COIN_ACCOUNT":
            [
    
            {"coin" :"BTCUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"ETHUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"XRPUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"ADAUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"DOGEUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"MATICUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"DOTUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"DAIUSDT" ,"amount" : 0,"dolar_eq" : 0},
            {"coin" :"SHIBUSDT" ,"amount" : 0,"dolar_eq" : 0},
            ]
}

    def Show_Balance(self):
        print("ACCOUNT BALANCE  \n-------------------\nCASH == " ,self.cash_balance)
        print("---------------")
        print("Coins")
        print(pd.DataFrame(self.coin_balance["COIN_ACCOUNT"]))
            

    def Buy_coin(self):
        
        
        
#result of the signal analysis will be bought with spesific amount
        
        

        
        pass



    def Sell_coin(self):
        pass
        
#if a coin is 1 percent up, sell it
#if a coin is down 0.5 percent, sell it
        
        
    def control_cash_amount(self):
        pass


        

       

        


    def Update_account(self):
        """
        refreshing the account every 1 sec
        
        """
        pass


pass


Account(1000).Show_Balance()

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

                
            
    






