import pandas as pd


class Account:

    def __init__(self,cash_balance,coin_balance = pd.DataFrame(columns=["coinname","amount","$"])):


        

        self.cash_balance = cash_balance

        self.coin_balance = coin_balance


    def Update_account(self):
        """
        refreshing the account every 1 sec
        
        """
    

