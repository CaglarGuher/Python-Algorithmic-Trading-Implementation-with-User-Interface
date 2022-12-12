from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import api2

#################### BINANCE API VARIABLES#####################


api_key = api2.Api_key2

api_secret = api2.Api_secret2

client = Client(api_key, api_secret)
###############################################################