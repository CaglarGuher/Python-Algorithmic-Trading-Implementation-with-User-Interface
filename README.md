# Crypto Trading Bot

This project is a cryptocurrency trading bot with a graphical user interface (GUI) built using Python. It allows users to fetch historical price data, visualize it with various parameters, and interact with their trading account on the Binance exchange. The bot uses Binance API, pandas, mplfinance, and PyQt5 libraries to manage data and create visualizations.

## Features

1. **Account and Asset Operations**: The bot can display a user's account information, including their total asset balance, cash balance, and individual coin balances.
2. **Data Preprocessing**: The bot processes data fetched from Binance API into pandas DataFrames and adjusts it for proper visualization and interaction.
3. **GUI**: The graphical user interface has various sections, including start/stop balance display, manual coin information, historical data visualization, and moving average settings.
4. **Historical Data Visualization**: The bot allows users to visualize historical price data with various parameters, such as moving averages, volume visualization, and different time intervals.
5. **Coin Information**: Users can fetch and display the current price of a given cryptocurrency.

## Components

1. **Account_Asset_Operation**: This component fetches and processes a user's account and asset information from Binance API and manages their balances. It includes classes such as `Account` and `Coin_Info_Response`, which handle interactions with the Binance API and manage the account's data.

2. **Df_adjusting_process**: This component adjusts the raw data fetched from Binance API into a pandas DataFrame, suitable for visualization and interaction. It includes functions like `give_df` and `give_current_price` that process and return the historical price data in the desired format.

3. **GUI (part1, part2, final part)**: These components are responsible for creating the graphical user interface using PyQt5. They define various widgets, such as buttons, labels, and text input fields, and connect them to their respective functions. The GUI is divided into different sections, such as start/stop balance display, manual coin information, historical data visualization, and moving average settings. The GUI also handles user interactions, like clicking buttons or entering text, and executes the corresponding functions.

4. **get_coin_info and Get_info**: These components are responsible for fetching historical price data, processing it, and generating visualizations using the mplfinance library. The `Get_info` class contains methods for setting the moving average values, price intervals, and other parameters for the visualization. It also provides methods for fetching and processing historical price data.

## Usage

To use the trading bot, first, install the required libraries:

```bash
pip install binance, pandas, mplfinance, PyQt5
```
Then, run the main script to launch the trading bot's graphical user interface. Input your Binance API key and secret, and interact with the various widgets to fetch historical price data, visualize it, and manage your trading account.

## License
This project is for educational purposes only. Users should exercise caution when using it with real trading accounts and ensure they understand the risks associated with trading cryptocurrencies. The authors of this project are not responsible for any potential losses incurred by users.
