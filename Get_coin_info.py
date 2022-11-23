from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import json
from datetime import datetime
import Api_code
import time
import mplfinance as mpf

#################### BINANCE API VARIABLES#####################
api_key = Api_code.api_key

api_secret = Api_code.api_secret

client = Client(api_key, api_secret)
###############################################################

class Get_info:

    def __init__(self , coinname , interval , startdate  , dataframe = []):
        '''
        format examples:
        coinname format = "BTCUSDT"
        interval format = "1m"
        fromtime format = 2020-06-06
        '''
        self.coinname =coinname
        self.interval = interval
        self.startdate = startdate
        self.dataframe = dataframe

############################################
    Client.KLINE_INTERVAL_1MONTH = "1m"
    Client.KLINE_INTERVAL_1WEEK = "1w"
    Client.KLINE_INTERVAL_1DAY = "1d"
    Client.KLINE_INTERVAL_12HOUR = "12h"
    Client.KLINE_INTERVAL_6HOUR = "6h"
    Client.KLINE_INTERVAL_4HOUR = "4h"
    Client.KLINE_INTERVAL_2HOUR = "2h"
    Client.KLINE_INTERVAL_1HOUR = "1h"
    Client.KLINE_INTERVAL_30MINUTE = "30min"
    Client.KLINE_INTERVAL_15MINUTE ="15min"
    Client.KLINE_INTERVAL_5MINUTE = "5min"
    Client.KLINE_INTERVAL_3MINUTE = "3min"
    Client.KLINE_INTERVAL_1MINUTE = "1min"
############################################
    def df(self):
       

        from_time = int(datetime.strptime(self.startdate, "%Y-%m-%d").timestamp()*1000)

        self.dataframe =  pd.DataFrame(client.get_historical_klines(self.coinname , self.interval , from_time))
        self.dataframe.columns = ["Opentime","Open","High","Low","Close","Volume","CloseTime","QuoteAssetTime","NumberOfTrades","VolumeOver24HourPeriod","PriceOver24HourPeriod ","Ignore"]
        columns_to_float = ["Open","High","Low","Close","Volume","NumberOfTrades"]
        self.dataframe[columns_to_float] =  self.dataframe[columns_to_float].astype(float)
        self.dataframe.drop(["Ignore","QuoteAssetTime","VolumeOver24HourPeriod","PriceOver24HourPeriod "],axis=1,inplace=True)
        self.dataframe["Opentime"] = pd.to_datetime(self.dataframe["Opentime"]/1000,unit ="s")
        self.dataframe["CloseTime"] = pd.to_datetime(self.dataframe["CloseTime"]/1000,unit ="s")

        return self.dataframe

        

    def current_price(self):
        return client.get_margin_price_index(symbol=self.coinname)["price"]

    def show_graph(self,a,b):
        Get_info.df(self)
        return mpf.plot(self.dataframe.set_index("CloseTime"),type = "line" ,style = "charles",mav =(a,b),volume = True)


a = Get_info(coinname="ETHUSDT",interval = "5min",startdate="2022-06-06")
print(a.df())

print(a.current_price())

print(a.show_graph(20,50))

###TESTING