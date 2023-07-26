import pandas as pd
import numpy as np
from binance.client import Client
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import gym
import gym_anytrading
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import A2C
from  available_coin_prices import COINS



class Signal_analysis():


    def __init__(self,api_key,api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def plot_real_vs_predicted(self,df, coin_name):
        plt.figure(figsize=(12, 6))

        df['day'] = df['timestamp'].dt.to_period('D')

        last_day_per_month = df.groupby('day').last()

        plt.plot(df['timestamp'], df['close'], label=f'Real {coin_name} Price', color='blue')
        plt.scatter(last_day_per_month['timestamp'], last_day_per_month['close'].where(last_day_per_month['Prediction'] == 1), label='Predicted Up', color='green', marker='^', alpha=1)
        plt.scatter(last_day_per_month['timestamp'], last_day_per_month['close'].where(last_day_per_month['Prediction'] == 0), label='Predicted Down', color='red', marker='v', alpha=1)

        plt.xlabel('Date')
        plt.ylabel(f'{coin_name} Price')
        plt.title(f'Real vs. Predicted {coin_name} Price per Month')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()



    def ma_predict_next_day_up(self,coin_name):
        client = Client(self.api_key, self.api_secret)
        symbol = f'{coin_name}'
        interval = Client.KLINE_INTERVAL_1DAY
        klines = client.get_klines(symbol=symbol, interval=interval,limit = 100000)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = df['close'].astype("float")
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        ma1_period = 5  
        ma2_period = 10
        df['MA1'] = df['close'].rolling(ma1_period).mean()
        df['MA2'] = df['close'].rolling(ma2_period).mean()
        df['target'] = df['close'].shift(-7)  
        df.dropna(inplace=True)
        train_df = df.iloc[:-100] 
        test_df = df.tail(100) 
        X_train = train_df[['MA1',"MA2",'close']]
        y_train = np.where(train_df['target'] > train_df['close'], 1, 0)  
        model = RandomForestClassifier(random_state=42,max_depth=12)
        model.fit(X_train, y_train)
        last_data = test_df[['MA1',"MA2",'close']]
        predictions = model.predict(last_data)
        current_predictions = predictions[-1]
        test_df['Prediction'] = predictions
        return test_df,current_predictions



    def calculate_rsi(self,data, period=14):
        data['close'] = data['close'].astype(float)
        close_price = data['close']
        delta = close_price.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi



    def bollinger_bands(self,df, window=20, k=2):
        df['Middle Band'] = df['close'].rolling(window=window).mean()
        df['Std Deviation'] = df['close'].rolling(window=window).std()
        df['Upper Band'] = df['Middle Band'] + (df['Std Deviation'] * k)
        df['Lower Band'] = df['Middle Band'] - (df['Std Deviation'] * k)
        return df




    def rsi_predict_next_day_up(self,coin_name):
        client = Client(self.api_key, self.api_secret)
        symbol = f'{coin_name}'
        interval = Client.KLINE_INTERVAL_1DAY

        klines = client.get_klines(symbol=symbol, interval=interval,limit = 100000)

        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = df['close'].astype(float)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['RSI'] = self.calculate_rsi(df)
        df['target'] = df['close'].shift(-7) 
        df.dropna(inplace=True)
        train_df = df.iloc[:-100] 
        test_df = df.tail(100) 

        X_train = train_df[['RSI', 'close']]
        y_train = np.where(train_df['target'] > train_df['close'], 1, 0) 
        model = RandomForestClassifier(random_state=42,max_depth=15)
        # Train the model
        model.fit(X_train, y_train)
        last_data = test_df[['RSI', 'close']]
        predictions = model.predict(last_data)
        current_predictions = predictions[-1]
        test_df['Prediction'] = predictions
        return test_df,current_predictions 
    
    def bollinger_predict_next_day_up(self,coin_name):
        client = Client(self.api_key, self.api_secret)
        symbol = f'{coin_name}'
        interval = Client.KLINE_INTERVAL_1DAY
        klines = client.get_klines(symbol=symbol, interval=interval,limit = 100000)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = df['close'].astype(float)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['RSI'] = self.calculate_rsi(df)
        window = 20
        k = 2
        df = self.bollinger_bands(df, window=window, k=k)
        df['target'] = df['close'].shift(-7)  
        df.dropna(inplace=True)
        train_df = df.iloc[:-100] 
        test_df = df.tail(100)   
        X_train = train_df[['close', 'Middle Band', 'Upper Band', 'Lower Band']]
        y_train = np.where(train_df['target'] > train_df['close'], 1, 0) 
        model = RandomForestClassifier(random_state=42,max_depth = 6)
        model.fit(X_train, y_train)
        last_data = test_df[[ 'close', 'Middle Band', 'Upper Band', 'Lower Band']]
        predictions = model.predict(last_data)
        current_predictions = predictions[-1]
        test_df['Prediction'] = predictions
        return test_df, current_predictions


    def reinforcement_signal(self,coin_name):
        client = Client(self.api_key, self.api_secret)
        symbol = f'{coin_name}'
        interval = Client.KLINE_INTERVAL_1DAY
        klines = client.get_klines(symbol=symbol, interval=interval,limit = 2000)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = df['close'].astype("float")
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        float_columns = ['open', 'high', 'low', 'volume', 'quote_asset_volume', 
                        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
        for col in float_columns:
            df[col] = df[col].astype(float)
        df['close_time'] = pd.to_datetime(df['close_time'])
        df.drop(columns=['quote_asset_volume', "close_time","number_of_trades",
                        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'],inplace=True)
        df.rename(columns={'timestamp': 'date'}, inplace=True)
        df.columns = df.columns.str.capitalize()
        df.set_index('Date', inplace=True)
        env = gym.make("stocks-v0",df = df,frame_bound = (10,100),window_size = 10) 
        env.signal_features[0:10]
        state = env.reset()
        while True:
            action = env.action_space.sample()
            n_state,reward,done,info = env.step(action)
            if done :
                print("info",info)
                break
        
        env.render_all()
        env_maker = lambda: gym.make("stocks-v0", df = df ,frame_bound =(10,100),window_size = 10)
        env = DummyVecEnv([env_maker])
        model = A2C("MlpPolicy",env,verbose = 1)
        model.learn(total_timesteps=10000)
        state = env.reset()
        buy_sell_signals = []
        while True: 
            action, _ = model.predict(state)
            buy_sell_signals.append(action)
            state, _, done, _ = env.step(action)
            if done:
                break
        buy_sell_signals = np.array(buy_sell_signals)
        return buy_sell_signals[-1]
    

    def overall_signal_rate(self,list):
        score_table = dict()
        for item in list:
            p1 = self.reinforcement_signal(item)[0]
            p2= self.bollinger_predict_next_day_up(item)[1]
            p3 = self.rsi_predict_next_day_up(item)[1]
            p4 = self.ma_predict_next_day_up(item)[1]
            item_score = p1+p2+p3+p4
            score_table[item] = item_score  
        return score_table
    

print(Signal_analysis(api_key="ZIuzde2gPV4OmU7ZQxmfbQ4m0ntSoaGMpLUgXe95vL3cAZVjcEThsOCFDtz041rO",
                api_secret="rEAT9OU3iYEN3bkvwtSjqWB1eVJflthuDN7q6MMNdXN94ngycqB0fBUi4IxlkNvv").overall_signal_rate(COINS))