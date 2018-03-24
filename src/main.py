import os
#from src.settings import INPUT_DATA,RAW_DATA
# from src.data_collection import request_all_crypto_pairs

# import data_collection
from data_collection import request_all_crypto_pairs, request_all_currencies, request_ticker_information
import time

'''
! check github keyword BITTREX for inspiration
https://www.reddit.com/r/BitcoinMarkets/comments/6k75ue/unable_to_get_historical_bittrex_data/
https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-WAVES&tickInterval=thirtyMin&_=1499127220008

This is the start of the creation of a trading bot.

The general plan follows these steps:

1. Data collection
    a. get the ticker and order book information from Bittrex
    b. store the data in csv files OR database
2. Create insights by visualizing the data
    a. create a dashboard
    b. create easy to change graphs
3. Create a hypothesis about:
    a. which KPI's should indicate markets where money is to be made
    b. which strategy to use to make money
4. Create the algorithm:
    a. based on signals (MACD, bollinger, moving averages)
    b. based on forecasts (other markets, forecasts)
5. Back-testing;
    a. calculate all the historical markets how the algo performed
6. Implement algo in realtime
    a. make sure it is robust!!

7. Adjust algo based on performance


'''

###### Initializaiton ######

## GLOBAL VARIABLES
#https://bittrex.com/fees
TRADING_FEE = 0.0025

# Retrieve all currency pairs on bittrex:
request_all_currencies()
crypto_market_pair_list = request_all_crypto_pairs()



start = time.time()
request_ticker_information(crypto_market_pair_list)
end = time.time()
print(end - start) # -- 136 on one run








if __name__ == "__main__":
    import sys
    # arg1 = sys.argv[1]
    # #function(sys.argv[1:])