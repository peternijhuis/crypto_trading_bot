'''
1. Data collection
    a. get the ticker and order book information from Bittrex
    b. store the data in csv files OR database
'''

import requests
import csv
import sys
import time


## -- all the currency pairs will be requested


def request_all_crypto_pairs():
    url_get_markets = 'https://bittrex.com/api/v1.1/public/getmarkets'
    r_crypto_markets = requests.get(url_get_markets, params=None)


    if r_crypto_markets.status_code != 200:
        # This means something went wrong.
        #todo log this error codes with timestamp
        print('ERROR: Requesting crypto pairs raises: {}'.format(r_crypto_markets.status_code))
    else:
        crypto_markets = r_crypto_markets.json()
        crypto_market_pair_list = []


        # writing all the crypto pairs to csv
        with open('crypto_pairs_registered.csv', 'w') as csvfile:
            fieldnames = list(crypto_markets['result'][0].keys())
            ''' For testing purpose write to output '''
            # crypto_markets_writer = csv.DictWriter(sys.stderr, fieldnames=fieldnames)
            crypto_markets_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            crypto_markets_writer.writeheader()
            for crypto_coins in crypto_markets['result']:
                crypto_market_pair_list.append(crypto_coins['MarketName'])
                crypto_markets_writer.writerow(crypto_coins)
        print('Number of crypto currency pairs trading: {}'.format(len(crypto_markets['result'])))
        return crypto_market_pair_list

def request_all_currencies():
    url_get_currencies = 'https://bittrex.com/api/v1.1/public/getcurrencies'
    r_crypto_currencies = requests.get(url_get_currencies, params=None)


    if r_crypto_currencies.status_code != 200:
        # This means something went wrong.
        #todo log this error codes with timestamp
        print('ERROR: Requesting crypto pairs raises: {}'.format(r_crypto_currencies.status_code))
    else:
        crypto_currencies = r_crypto_currencies.json()

        # writing all the crypto pairs to csv
        with open('crypto_currencies_details.csv', 'w') as csvfile:
            fieldnames = list(crypto_currencies['result'][0].keys())
            ''' For testing purpose write to output '''
            # crypto_markets_writer = csv.DictWriter(sys.stderr, fieldnames=fieldnames)
            crypto_currencies_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            crypto_currencies_writer.writeheader()
            for crypto_coins in crypto_currencies['result']:
                crypto_currencies_writer.writerow(crypto_coins)

        print('Number of crypto currencies trading: {}'.format(len(crypto_currencies['result'])))
        return



def request_ticker_information(crypto_market_list):

    url_get_ticker = 'https://bittrex.com/api/v1.1/public/getticker'

    for pair in crypto_market_list:
        print(pair)
        ticker_value = {'market': pair}
        # ticker_value = {'market': 'BTC-LTC'}
        time.sleep(1)
        r_crypto_tickers = requests.get(url_get_ticker, params=ticker_value)
        print(r_crypto_tickers.json())



    # if r_crypto_pairs.status_code != 200:
    #     # This means something went wrong.
    #     #todo log this error codes with timestamp
    #     print('ERROR: Requesting crypto pairs raises: {}'.format(r_crypto_pairs.status_code))
    # else:
    #     crypto_pairs_response = r_crypto_pairs.json()
    #
    #     # writing all the crypto pairs to csv
    #     with open('crypto_pairs_registered.csv', 'w') as csvfile:
    #         fieldnames = list(crypto_pairs_response['result'][0].keys())
    #         ''' For testing purpose write to output '''
    #         # crypto_pair_writer = csv.DictWriter(sys.stderr, fieldnames=fieldnames)
    #         crypto_pair_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         crypto_pair_writer.writeheader()
    #         for crypto_coins in crypto_pairs_response['result']:
    #                 crypto_pair_writer.writerow(crypto_coins)




# request_all_crypto_pairs()

# request_ticker_information()