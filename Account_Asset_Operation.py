import pandas as pd
from Get_coin_info import Get_info as GI
import time
import json
from available_coin_prices import COINS
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

# Assuming the required classes and functions are imported her

class Account():

    def __init__(self,api_key,api_secret, cash_balance=0, total_balance=0):
        super().__init__()
        self.cash_balance = cash_balance
        self.total_balance = total_balance
        self.api_key = api_key
        self.api_secret = api_secret

        client = Client(self.api_key, self.api_secret)
        
        self.info = client.get_account()

        self.coin_account = {
            "COIN_ACCOUNT": []
        }
        self.a = []
        for i in range(0, len(COINS)):
            RES = COINS[i].replace("USDT", "")
            self.a.append(RES)
        for i in range(0, len(self.info["balances"])):
            if self.info["balances"][i]["asset"] in self.a:
                if float(self.info["balances"][i]["free"]) > 0:
                    self.coin_account["COIN_ACCOUNT"].append({
                        "coin": (self.info["balances"][i]["asset"] + "USDT"),
                        "coin_amt": float(self.info["balances"][i]["free"]),
                        "dolar_eq": "%.3f" % (float(self.info["balances"][i]["free"]) * float(GI(api_secret = self.api_secret,api_key =self.api_key,coinname=(self.info["balances"][i]["asset"] + "USDT")).give_current_price()))
                    })

    def Buy_signal_coin(self, bought_coin):
        # Implement the Buy_signal_coin method here
        pass
    def give_coin_balance(self):
        return self.coin_account["COIN_ACCOUNT"]
    def show_total_balance(self):
        self.total_balance = 0
        for data in self.coin_account["COIN_ACCOUNT"]:
            self.total_balance += float(data["coin_amt"]) * (GI(api_secret = self.api_secret,api_key =self.api_key,coinname=(data["coin"])).give_current_price())
        self.total_balance += self.cash_balance
        return "%.3f" % self.total_balance
    def show_cash_balance(self):
        for i in range(0, len(self.info["balances"])):
            if self.info["balances"][i]["asset"] == "USDT":
                self.cash_balance = float(self.info["balances"][i]["free"])
        return self.cash_balance




 
        






        

       

        


   


    

                
            
    



      

    

    
    
    







