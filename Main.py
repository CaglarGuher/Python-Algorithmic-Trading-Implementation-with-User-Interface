from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import json
from datetime import datetime
import seaborn as sns
import mplfinance as mpf



class Monitorizing:
    
    pass



#Logging
## deeneme deneme

class Account:
    
    
    pass






class Asset_Operation():
    
    pass


class Decision_Analysis():


    api_key = "API_KEY"

    api_secret = "API_SECRET"

    client = Client(api_key, api_secret)

    def coin_info(coinname,interval,fromtime):
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
        from_time = int(datetime.strptime(fromtime, "%Y-%m-%d").timestamp()*1000)
        df =  pd.DataFrame(client.get_historical_klines(coinname, interval ,from_time))
        df.columns = ["Opentime","Open","High","Low","Close","Volume","CloseTime","QuoteAssetTime","NumberOfTrades","VolumeOver24HourPeriod","PriceOver24HourPeriod ","Ignore"]
        columns_to_float = ["Open","High","Low","Close","Volume","NumberOfTrades"]
        df[columns_to_float] =  df[columns_to_float].astype(float)
        df.drop(["Ignore","QuoteAssetTime","VolumeOver24HourPeriod","PriceOver24HourPeriod "],axis=1,inplace=True)
        df["Opentime"] = pd.to_datetime(df["Opentime"]/1000,unit ="s")
        df["CloseTime"] = pd.to_datetime(df["CloseTime"]/1000,unit ="s")

        return df 
    def current_price(coinname):
        return client.get_margin_price_index(symbol='NEOUSDT')["price"]

    def coin_visual(dataframe,a,b):
        return mpf.plot(dataframe.set_index("CloseTime"),type = "line" ,style = "charles",mav =(a,b),volume = True)


    ##it will continue as researched##
     



class Web_Socket:

    pass





class Gui:

    pass