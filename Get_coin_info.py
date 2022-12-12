import pandas as pd
import json
from datetime import datetime
import api2
import time
import mplfinance as mpf
from api_access import client , Client

class Get_info():

    def __init__(self , coinname ,  startdate ="01.01.2021" , 
    interval = "4h" ,  dataframe = [], show_volume = False,show_ma = False, ma1 = 0 , ma2 = 0):
        '''
        format examples:
        coinname format = "BTCUSDT"
        interval format = "1m"
        fromtime format = "2020-06-06"
        '''
        self.coinname =coinname
        self.interval = interval
        self.startdate = startdate
        self.dataframe = dataframe
        self.ma1 = ma1
        self.ma2 = ma2
        self.show_volume = show_volume
        self.show_ma = show_ma
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
    def give_df(self):
       

        from_time = int(datetime.strptime(self.startdate, "%Y-%m-%d").timestamp()*1000)

        self.dataframe =  pd.DataFrame(client.get_historical_klines(self.coinname , self.interval , from_time))
        self.dataframe.columns = ["Opentime","Open","High","Low","Close","Volume","CloseTime","QuoteAssetTime","NumberOfTrades","VolumeOver24HourPeriod","PriceOver24HourPeriod ","Ignore"]
        columns_to_float = ["Open","High","Low","Close","Volume","NumberOfTrades"]
        self.dataframe[columns_to_float] =  self.dataframe[columns_to_float].astype(float)
        self.dataframe.drop(["Ignore","QuoteAssetTime","VolumeOver24HourPeriod","PriceOver24HourPeriod "],axis=1,inplace=True)
        self.dataframe["Opentime"] = pd.to_datetime(self.dataframe["Opentime"]/1000,unit ="s")
        self.dataframe["CloseTime"] = pd.to_datetime(self.dataframe["CloseTime"]/1000,unit ="s")

        return self.dataframe

        

    def give_current_price(self ):

        return float(client.get_margin_price_index(symbol=self.coinname)["price"])

       


    

    def set_ma1_value(self,ma1 = int):

        self.ma1 = ma1
        return self.ma1

    

    def set_ma2_value(self,ma2 = int):
        
        self.ma2 = ma2
        return self.ma2

    

    def hist_data_start_date(self,startdate):

        self.startdate = startdate

        return self.startdate
    
    
    def set_volume_visualization(self,show_volume):

        self.show_volume = show_volume

        return  self.show_volume

        
        

    def set_price_interval(self,interval):

        self.interval = interval

        return self.interval



    def show_graph(self,show_ma):

        self.show_ma = show_ma

        Get_info.give_df(self)
        
        if self.show_ma :
            

            return mpf.plot(self.dataframe.set_index("CloseTime"),type = "line" ,style = "charles",mav =(self.ma1,self.ma2),volume = self.show_volume)
        
        else:


            return mpf.plot(self.dataframe.set_index("CloseTime"),type = "line" ,style = "charles",volume = self.show_volume)




