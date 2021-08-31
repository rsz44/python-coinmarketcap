#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2019 Remi SARRAZIN
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import logging
from logging.config import dictConfig
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

VERSION = "0.3"
SANDBOX_API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'f': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['h'],
        'level': logging.DEBUG,
    }
}


class APITimer(object):
    """APITimer"""

    def __init__(self):
        self.__t = time.time()

    def reset(self):
        self.__t = time.time()

    @property
    def elapsed(self):
        return time.time() - self.__t


class Response(object):
    """Response"""

    def __init__(self, resp, timer):
        self.__payload = json.loads(resp.text)
        self.__timer = timer
        self._message = self.__payload.get('message', None)
        self._error = self.__payload.get('error', None)
        self._statusCode = self.__payload.get('statusCode', None)
        if self._message and self._error and self._statusCode:
            self.status = {
                'error_code': self._statusCode,
                'error_message': self._message,
            }
        else:
            self.status = self.__payload.get('status', {})

        self.data = self.__payload.get('data', {})
        self.timesamp = self.status.get('timestamp', None)
        self.error_code = self.status.get('error_code', None)
        self.error_message = self.status.get('error_message', None)
        self.error = True if self.error_code and self.error_message else False
        self.ok = False if self.error else True
        self.elapsed = self.status.get('elapsed', None)
        self.credit_count = self.status.get('credit_count', None)
        self.__time_snap = timer.elapsed

    @property
    def total_elapsed(self):
        """
          Total request time
        """
        return self.__time_snap

    def __repr__(self):
        if self.error:
            status = 'ERR {} "{}"'.format(self.error_code, self.error_message)
        else:
            status = 'OK'
        data = repr(self.data)
        return 'RESPONSE: {:.0f}ms {}: {}'.format(
            self.__time_snap*1000, status, data)

    def __str__(self):
        return self.__repr__()


class CoinMarketCapAPIError(Exception):
    """CoinMarketCapAPIError"""

    def __init__(self, r):
        super(CoinMarketCapAPIError, self).__init__(repr(r))
        self.rep = r


class CoinMarketCapAPI(object):
    """CoinMarketCapAPI Wrapper Class"""

    def __init__(self, api_key=None, **kwargs):
        self.__session = Session()
        self.__logger = kwargs.get('logger', None)
        self.__debug = kwargs.get('debug', False)

        if not self.__logger and self.__debug:
            dictConfig(LOGGING_CONFIG)
            self.__logger = logging.getLogger()

        self.__version = kwargs.get('version', 'v1')

        if api_key is None:
            self.__sandbox = True
            self.__key = SANDBOX_API_KEY
        else:
            self.__sandbox = kwargs.get('sandbox', False)
            self.__key = api_key

        if self.__sandbox:
            self.__base_url = 'https://sandbox-api.coinmarketcap.com/'
        else:
            self.__base_url = 'https://pro-api.coinmarketcap.com/'

        self.__headers = {
            'Accepts': 'application/json',
            'Accept-Encoding': 'deflate, gzip',
            'X-CMC_PRO_API_KEY': api_key
        }

    def __get(self, url, **kwargs):
        timer = APITimer()

        if self.__debug:
            self.__logger.debug('GET {} {}\nPARAMETERS: {}'.format(
                'SANDBOX' if self.__sandbox else 'PRO',
                repr(url), repr(kwargs)))

        self.__session.headers.update(self.__headers)
        version = kwargs.pop('api_version', self.__version)
        url = '{}{}{}'.format(self.__base_url, version, url)

        try:
            response = self.__session.get(url, params=kwargs)
            rep = Response(response, timer)
            if self.__debug:
                self.__logger.debug(rep)
            if rep.error:
                if rep.error_code == 401 and \
                    "API Key is invalid" in rep.error_message and \
                        self.__debug:

                    ak = 'sandbox-api' if self.__sandbox else 'pro-api'
                    self.__logger.warning(
                        'Be sure you are using a {} key or set `sandbox={}`'
                        .format(ak, not self.__sandbox) +
                        ' to CoinMarketCapAPI, see issue #1.')

                raise CoinMarketCapAPIError(rep)
            return rep
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            self.__logger.warning(e)
            raise e

    def cryptocurrency_map(self, **kwargs):
        """
          CoinMarketCap ID map
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        return self.__get(
            '/cryptocurrency/map',
            **kwargs)

    def cryptocurrency_info(self, **kwargs):
        """
          Metadata
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        """
        return self.__get(
            '/cryptocurrency/info',
            **kwargs)

    def cryptocurrency_listings_latest(self, **kwargs):
        """
          Latest listings
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
        """
        return self.__get(
            '/cryptocurrency/listings/latest',
            **kwargs)

    def cryptocurrency_listings_historical(self, **kwargs):
        """
          Historical listings
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical
        """
        return self.__get(
            '/cryptocurrency/listings/historical',
            **kwargs)

    def cryptocurrency_quotes_latest(self, **kwargs):
        """
          Latest quotes
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
        """
        return self.__get(
            '/cryptocurrency/quotes/latest',
            **kwargs)

    def cryptocurrency_quotes_historical(self, **kwargs):
        """
          Historical quotes
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesHistorical
        """
        return self.__get(
            '/cryptocurrency/quotes/historical',
            **kwargs)

    def cryptocurrency_marketpairs_latest(self, **kwargs):
        """
          Latest market pairs
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest
        """
        return self.__get(
            '/cryptocurrency/market-pairs/latest',
            **kwargs)

    def cryptocurrency_ohlcv_latest(self, **kwargs):
        """
          Latest OHLCV
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvLatest
        """
        return self.__get(
            '/cryptocurrency/ohlcv/latest',
            **kwargs)

    def cryptocurrency_ohlcv_historical(self, **kwargs):
        """
          Historical OHLCV
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvHistorical
        """
        return self.__get(
            '/cryptocurrency/ohlcv/historical',
            **kwargs)

    def cryptocurrency_priceperformancestats_latest(self, **kwargs):
        """
          Price performance Stats
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyPriceperformancestatsLatest
        """
        return self.__get(
            '/cryptocurrency/price-performance-stats/latest',
            **kwargs)

    def cryptocurrency_categories(self, **kwargs):
        """
          Categories
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategories
        """
        return self.__get(
            '/cryptocurrency/categories',
            **kwargs)

    def cryptocurrency_category(self, **kwargs):
        """
          Category
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory
        """
        return self.__get(
            '/cryptocurrency/category',
            **kwargs)

    def cryptocurrency_airdrops(self, **kwargs):
        """
          Airdrops
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrops
        """
        return self.__get(
            '/cryptocurrency/airdrops',
            **kwargs)

    def cryptocurrency_airdrop(self, **kwargs):
        """
          Airdrop
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrop
        """
        return self.__get(
            '/cryptocurrency/airdrop',
            **kwargs)

    def cryptocurrency_trending_latest(self, **kwargs):
        """
          Trending Latest
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingLatest
        """
        return self.__get(
            '/cryptocurrency/trending/latest',
            **kwargs)

    def cryptocurrency_trending_mostvisited(self, **kwargs):
        """
          Trending Most Visited
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingMostvisited
        """
        return self.__get(
            '/cryptocurrency/trending/most-visited',
            **kwargs)

    def cryptocurrency_trending_gainerslosers(self, **kwargs):
        """
          Trending Gainers & Losers
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingGainerslosers
        """
        return self.__get(
            '/cryptocurrency/trending/gainers-losers',
            **kwargs)

    def exchange_map(self, **kwargs):
        """
          CoinMarketCap ID map
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMap
        """
        return self.__get(
            '/exchange/map',
            **kwargs)

    def exchange_info(self, **kwargs):
        """
          Metadata
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo
        """
        return self.__get(
            '/exchange/info',
            **kwargs)

    def exchange_listings_latest(self, **kwargs):
        """
          Latest listings
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsLatest
        """
        return self.__get(
            '/exchange/listings/latest',
            **kwargs)

    def exchange_listings_historical(self, **kwargs):
        """
          Historical listings
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsHistorical
        """
        return self.__get(
            '/exchange/listings/historical',
            **kwargs)

    def exchange_quotes_latest(self, **kwargs):
        """
          Latest quotes
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesLatest
        """
        return self.__get(
            '/exchange/quotes/latest',
            **kwargs)

    def exchange_quotes_historical(self, **kwargs):
        """
          Historical quotes
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesHistorical
        """
        return self.__get(
            '/exchange/quotes/historical',
            **kwargs)

    def exchange_marketpairs_latest(self, **kwargs):
        """
          Latest market pairs
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest
        """
        return self.__get(
            '/exchange/market-pairs/latest',
            **kwargs)

    def globalmetrics_quotes_latest(self, **kwargs):
        """
          Latest global metrics
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest
        """
        return self.__get(
            '/global-metrics/quotes/latest',
            **kwargs)

    def globalmetrics_quotes_historical(self, **kwargs):
        """
          Historical global metrics
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical
        """
        return self.__get(
            '/global-metrics/quotes/historical',
            **kwargs)

    def tools_priceconversion(self, **kwargs):
        """
          Price conversion tool
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion
        """
        return self.__get(
            '/tools/price-conversion',
            **kwargs)

    def blockchain_statistics_latest(self, **kwargs):
        """
          Latest statistics
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1BlockchainStatisticsLatest
        """
        return self.__get(
            '/blockchain/statistics/latest',
            **kwargs)

    def fiat_map(self, **kwargs):
        """
          CoinMarketCap ID map
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap
        """
        return self.__get(
            '/fiat/map',
            **kwargs)

    def partners_flipsidecrypto_fcas_listings_latest(self, **kwargs):
        """
          List all available FCAS scores
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasListingsLatest
        """
        return self.__get(
            '/partners/flipside-crypto/fcas/listings/latest',
            **kwargs)

    def partners_flipsidecrypto_fcas_quotes_latest(self, **kwargs):
        """
          Request specific FCAS scores
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasQuotesLatest
        """
        return self.__get(
            '/partners/flipside-crypto/fcas/quotes/latest',
            **kwargs)

    def key_info(self, **kwargs):
        """
          Key Info
          See also :
          https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo
        """
        return self.__get(
            '/key/info',
            **kwargs)
