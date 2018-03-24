#! /usr/bin/env python
import json
import os
import time
from datetime import datetime
import requests
import sys

# locate the root folder
root_folder_project = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# add the root folder to sys path, this way the different modules can be imported by terminal!
sys.path.insert(1, root_folder_project)

from src.settings import RAW_DATA


# todo make robust on request, catch exceptions
# todo write script to aggregate and remove old files
# todo schedule as cronjob
# todo place logging at different folder

#"volumeto" means the volume in the currency that is being traded (currency volume)
#"volumefrom" means the volume in the base currency that things are traded into. (bitcoin volume)

# Collect the past day(+) and overwrite the double requested to create certainty in overlap
def request_last_day(ticker):
    url_get_minute_OHLCV = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym=BTC&limit=1500&aggregate=1&e=BITTREX'.format(ticker)
    r_crypto_currencies = requests.get(url_get_minute_OHLCV, params=None)

    if r_crypto_currencies.status_code != 200:
        # This means something went wrong in requesting.
        # Try after sleep of ~1 minute
        time.sleep(62)
        r_crypto_currencies = requests.get(url_get_minute_OHLCV, params=None)

        if r_crypto_currencies.status_code != 200:
            logfile = '{}_{}_scrape_error.log'.format(str(datetime.now().strftime("%Y%m%d_%H%M%S")), ticker)
            folder = os.path.join(RAW_DATA, '_logfiles')
            if not os.path.exists(folder):
                os.makedirs(folder)
            logf = open(os.path.join(folder, logfile), "w")
            logf.write(
                "Failed to request {0}. Status code: {1}. Time: {2}\n".format(ticker, r_crypto_currencies.status_code,
                                                                              str(datetime.now().strftime("%Y%m%d_%H%M%S"))))
        else:
            # function do stuff with requests
            _check_content_request(r_crypto_currencies, ticker)

    else:
        # function do stuff with requests
        _check_content_request(r_crypto_currencies, ticker)


def _check_content_request(request, ticker):
    d = request.json()
    if d['Response'] == 'Error':
        logfile = '{}_{}_request_error.log'.format(str(datetime.now().strftime("%Y%m%d_%H%M%S")), ticker)
        folder = os.path.join(RAW_DATA, '_logfiles')
        if not os.path.exists(folder):
            os.makedirs(folder)
        logf = open(os.path.join(folder, logfile), "w")
        logf.write("{}. Time: {}\n".format(d['Message'], str(datetime.now().strftime("%Y%m%d_%H%M%S"))))
    else:
        # function save data
        _save_ticker_data(d, ticker)


def _save_ticker_data(ticker_data, ticker):
    ticker_data_json = {'TimeFrom': ticker_data['TimeFrom'], 'TimeTo': ticker_data['TimeTo'],
                        'Data': ticker_data['Data']}
    folder = os.path.join(RAW_DATA, ticker)
    start = time.strftime("%Y%m%d_%H%M%S", time.localtime(ticker_data['TimeFrom']))
    end = time.strftime("%Y%m%d_%H%M%S", time.localtime(ticker_data['TimeTo']))

    filename = '{}_to_{}_{}_OHLCV.json'.format(start, end, ticker)
    path = os.path.join(folder, filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(path, 'w') as fp:
        json.dump(ticker_data_json, fp, sort_keys=True, indent=4)

# Manual list:
list_of_currencies = ['ADA', 'DOGE', 'ETH', 'LRC', 'LTC', 'NEO', 'NXS', 'OMG', 'PIVX', 'POWR', 'QRL', 'QTUM', 'SC', 'SNT', 'STRAT', 'TRX', 'XMR', 'XRP', 'XVG']
for currency in list_of_currencies:
    request_last_day(currency)
    print("{} finished".format(currency))
    time.sleep(1)


# r = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies', params=None)
# # print(r.json())
#
# # 294 crypto's on Bittrex:
# for currencies in r.json()['result']:
#     # print(currencies['Currency'])
#     request_last_day(currencies['Currency'])
#     print("{} finished".format(currencies['Currency']))
#     time.sleep(.25) ## --> to not hit the 5 per second (300 a minute)


'''

Usage:
1. 25 hours requested

2. Get open, high, low, close, volumefrom and volumeto from the each minute historical data. 
It uses BTC conversion if data is not available because the coin is not trading in the specified currency.


3. Info
Caching	        40 seconds
Rate limits	    Hour limit - 8000, Minute limit - 300, Second limit - 15

4. Examples
https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=60&aggregate=3&e=CCCAGG


'''
