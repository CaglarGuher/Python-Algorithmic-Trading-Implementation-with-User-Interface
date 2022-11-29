
from Get_coin_info import Get_info as GI
import pandas as pd
import mplfinance as mpf
import random
import time


'''
It will be a simple signal analysis
it will check the ma crossections
when double ma crossection occurs(ma20 and ma50 for now)
in will send "buy signal" to Asset Operation
Class will check 10 main coin as mentioned:
BTC,ETH,BNB,XRP,ADA,DOGE,MATIC,DOT,DAI,SHIB
'''



class Signal_Analysis():


    

    
    def __init__(self,suggested_coin = ""):


        self.suggested_coin = suggested_coin
    
    


    '''
    it will initialize every 1 min 

    for now,random coin will be suggested every 1 min and send it to Asset Operation
    '''





    


    def coin_checker(self):
        pass




    def MA_Analysis(self,dataframe):

        pass


    def Analysis2(self):

        pass


    def Analysis3(self):

        pass

    
    def Analysis4(self):

        pass

    
    def suggest_random_coin(self):

        coin_names = ["BTCUSDT","ETHUSDT","BNBUSDT","XRPUSDT","ADAUSDT","DOGEUSDT","MATICUSDT","DOTUSDT","DAIUSDT","SHIBUSDT"]

        self.suggested_coin = coin_names[random.randint(0,len(coin_names)-1)]

        return self.suggested_coin
        
       
        
    pass









       



    
        


    
##In the end as a test, signal analysis will give signal to a coin if ma10 cross ma20 from below
## to make that happen in a small period of time,it will check every min
            


##testing

        

        




        

        



 
    


