import pandas as pd
from Signal_Analysis import Signal_Analysis
from Get_coin_info import Get_info as GI
import time
import json
from api_access import client
from available_coin_prices import COINS


class Account(Signal_Analysis):

    def __init__(self,cash_balance = 0 , total_balance = 0):

        super().__init__(Signal_Analysis)

        self.cash_balance = cash_balance

        self.total_balance = total_balance

        self.info = client.get_account()


        self.coin_account = {
                "COIN_ACCOUNT":
                [{"coin" :"BTCUSDT" ,"coin_amt" : 0,}]
                } 
                  
        self. a = []

        for i in range(0,len(COINS)):

            RES = COINS[i].replace("USDT","")
            self.a.append(RES)




       
        for i in range(0,len(self.info["balances"])):

            if self.info["balances"][i]["asset"] in self.a:

                if float(self.info["balances"][i]["free"]) > 0:
                    self.coin_account["COIN_ACCOUNT"].append({"coin" :(self.info["balances"][i]["asset"]+"USDT") ,"coin_amt" : float(self.info["balances"][i]["free"])})
            
        


    def Buy_signal_coin(self,bought_coin):
        
        pass
             



###############################

    def show_bought_coin(self):
        pass


    def give_coin_balance(self):


        return self.coin_account["COIN_ACCOUNT"]


    def show_total_balance(self):

        self.total_balance = 0

        for data in self.coin_account["COIN_ACCOUNT"]:
            self.total_balance = self.total_balance + float(data["coin_amt"])*(GI((data["coin"])).give_current_price())

        self.total_balance = self.total_balance + self.cash_balance

        return self.total_balance

    def show_amt_coin_bought(self):

         pass


    def show_cash_balance(self):
        for i in range (0,len(self.info["balances"])):

            if self.info["balances"][i]["asset"] == "USDT":
                self.cash_balance = float(self.info["balances"][i]["free"])
        return self.cash_balance




 
        






        

       

        


   


    

                
            
    



      

    

    
    
    







