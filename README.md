# PyTrade
# INITIALIZATION OF THE PYTRADE
# BETA VERSION

 " building a real time coin tracking and automatized trading algorthim "

 IT WILL CONSIST :

- An account with fake money
- Spot account,
- Multiple trading algorithms,
- Short period(1 Day) buy-hold-sell automatization,
- Risk management,
- Manual trading options ( This is optional for now )
  - - reason : observing ; alghoritms vs human instints
- Real time monitorizing the results
 -------



# PACKAGES
- LOGGING  
- PANDAS 
- SCIKIT LEARN ---
- BEAUTIFULSOUP---
- API READER(WILL DECIDE LATER)---
- SEABORN OR MATHPLOTLIB OR OTHER VISUALIZATION PACKAGE ---
    





# LOGGING
+ It is a clear visualization of logging process

+ we will clearly see from every decision that the alghoritm makes to our current balance


class Monitorizing:
    
    pass



----------------------------

# Account

+ Simple account class that will keep tracking our Acoount



class Account:
    
    pass


+ Cash balance will be a single number currency as a dolar(for now)
Initial balance will be 1000USDT

+ Asset balance will be list consist of current assets with their amount

- Warning 
!!!!because the code wont be executed in a server , we should save the balance in a database, and 
after re-executing , the system should read account datas from the database before starting the algorithm


# Asset Operation


class Asset_Operation():
    
    pass
# Get_coin_info
this class will get the required information for decision analysis


# Decision Analysis


+ Signal Analysis class will be  the brain of the  algortihm
+ ALL DECISIONS WILL BE MADE IN THIS CLASS


class Signal_Analysis():
    

    def ML_analysis():
        pass

    def Pop_analysis():
        pass
    
    def grap_analysis():
        pass

- (it will continue as researched)
     

- For now, there will be only 10 main coin analysis with binance api code,
BTC,ETH,BNB,XRP,ADA,DOGE,MATIC,DOT,DAI,SHIB with USDT parity
Later, there will be every coin taken from coin.api website

- There will be multiple instances coming out from this class as a result of
the analysis (best buy options for daily,weekly,montly)
best selling options
stop loss warnings etc...



+ ANALYSIS PART...
IF conditions == True:
    self.suggested = suggested (as a single string output)

- ----------------------------------------------------------





# AFTER THE BETA VERSION OF THE ALGORITHM IS COMPLETED!!!!

+ LATER WHEN SERVER CONNECTION IS SECURED, IT WILL LET US CONNECT TO THE SERVER

* # -------Server Implementation---------

class Web_Socket:

    pass



# Interface



class Gui:

    pass

