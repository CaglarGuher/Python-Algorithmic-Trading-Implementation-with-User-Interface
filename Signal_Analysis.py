
from Get_coin_info import Get_info as GI
import pandas as pd
import mplfinance as mpf


'''
It will be a simple signal analysis
it will check the ma crossections
when double ma crossection occurs(ma20 and ma50 for now)
in will send "buy signal" to Asset Operation
Class will check 10 main coin as mentioned:
BTC,ETH,BNB,XRP,ADA,DOGE,MATIC,DOT,DAI,SHIB
'''



class Signal_Analysis():
    
    Testing = True


    '''
    it will initialize every 1 min 

    
    
    '''


    coin_names = ["BTCUSDT","ETHUSDT","BNBUSDT","XRPUSDT","ADAUSDT","DOGEUSDT","MATICUSDT","DOTUSDT","DAIUSDT","SHIBUSDT"]


    '''For now, coins will be checked manually inside a list.
        After all the past datas are send to big database(mongodb or mysql)
        every coin will be checked automatically     
    '''
    


    def MA_Analysis(self,dataframe):

        self.dataframe = dataframe
        ma10 = self.dataframe["Close"].rolling(10).mean().values
        ma20 = self.dataframe["Close"].rolling(20).mean().values
        testing = pd.DataFrame(dict(OpMav10=ma10,OpMav20=ma20),index=self.dataframe.index)
        ##testing##
        
        for i in range(0,len(testing)):

            first_crossection = 0
            if ma10[i] > ma20[i]:
                print("ma10:{ma10} is greater than ma20:{ma20}")
                first_crossection = 1
            if ma20[i] > ma10[i]:
                print("ma10:{ma10} is less than ma20:{ma20}")
##In the end as a test, signal analysis will give signal to a coin if ma10 cross ma20 from below
## to make that happen in a small period of time,it will check every min
            


##testing
test1 = Signal_Analysis()
B = GI(coinname="ETHUSDT",interval = "15min",startdate="2022-01-01")

print(test1.MA_Analysis(B.df()))
print(B.show_graph(10,20))
        
        

        




        

        



 
    


