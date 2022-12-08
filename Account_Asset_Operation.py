import pandas as pd
from Signal_Analysis import Signal_Analysis
from Get_coin_info import Get_info as GI
import time
import json



class Account(Signal_Analysis):

    def __init__(self , cash_balance ,coin_balance = 0  ):

        super().__init__(Signal_Analysis)

        self.coin_balance = coin_balance
        
        self.cash_balance = cash_balance
        

        self.coin_account = {
            "COIN_ACCOUNT":
            [
    
            {"coin" :"BTCUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"ETHUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"XRPUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"ADAUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"DOGEUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"MATICUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"DOTUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"DAIUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"SHIBUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            {"coin" :"BNBUSDT" ,"amt" : 0,"$" : 0 ,"$/unit" : 0},
            ]

}   

    



    def Buy_signal_coin(self,bought_coin):
        
        self.bought_coin = bought_coin
       
        for data in self.coin_account["COIN_ACCOUNT"]:
            
            if data["coin"] == self.bought_coin :

                if data["amt"] == 0:

                    data["amt"] = data["amt"] +  (self.cash_balance * 0.1)/GI(self.bought_coin).give_current_price()
                    data["$"] = self.cash_balance * 0.1
                    data["$/unit"] = GI(self.bought_coin).give_current_price()

                    self.cash_balance = self.cash_balance -  self.cash_balance * 0.1



    def calculate_total_balance(self):

        for data in self.coin_account["COIN_ACCOUNT"]: 
            self.coin_balance = self.coin_balance + (data["amt"] * GI(data["coin"]).give_current_price()) 
        self.total_balance = self.cash_balance + self.coin_balance
        self.coin_balance  = 0
        



###############################

    def show_bought_coin(self):
        return self.bought_coin


    def give_coin_balance(self):


        return self.coin_account["COIN_ACCOUNT"]


    def show_total_balance(self):

        return self.total_balance


    def show_amt_coin_bought(self):

         return ((self.cash_balance * 0.1)/GI(self.bought_coin).give_current_price()) , self.bought_coin 


    def show_cash_balance(self):
        return self.cash_balance



    

 
        






        

       

        


   


    

                
            
    



      

    

    
    
    







