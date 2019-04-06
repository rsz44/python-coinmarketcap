#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.config import dictConfig
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

VERSION="0.1"
LOGGING_CONFIG = {  
  'version': 1,
  'formatters':{
    'f': {
      'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    }
  },
  'handlers':{
    'h': {
      'class': 'logging.StreamHandler',
      'formatter': 'f',
      'level': logging.DEBUG
    }
  },
  'root':{
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
    status = 'ERR {} "{}"'.format(self.error_code, self.error_message) if self.error else 'OK'
    data = repr(self.data)
    #print repr(self.__payload)
    return 'RESPONSE: {:.0f}ms {}: {}'.format(self.__time_snap*1000, status, data)

  def __str__(self):
    return self.__repr__()

class CoinMarketCapAPIError(Exception):
  """CoinMarketCapAPIError"""
  def __init__(self, r):
    super(CoinMarketCapAPIError, self).__init__(repr(r))
    self.rep = r

class CoinMarketCapAPI(object):
   

  """CoinMarketCapAPI Wrapper Class"""
  def __init__(self, api_key, **kwargs):
    self.__session = Session()
    self.__logger = kwargs.get('logger', None)
    self.__debug = kwargs.get('debug', False)

    if not self.__logger and self.__debug:
      dictConfig(LOGGING_CONFIG)
      self.__logger = logging.getLogger()

    self.__version = kwargs.get('version', 'v1')
    self.__sandbox = kwargs.get('sandbox', True)
    self.__key = api_key
    self.__base_url = 'https://sandbox-api.coinmarketcap.com/' if self.__sandbox else 'https://pro-api.coinmarketcap.com/'
    self.__headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

  def __get(self, url, **kwargs):
    timer = APITimer()
    
    if self.__debug:
      self.__logger.debug('GET {} {}\nPARAMETERS: {}'.format( 'SANDBOX' if self.__sandbox else 'PRO', repr(url), repr(kwargs) ))

    self.__session.headers.update(self.__headers)
    url = '{}{}'.format(self.__base_url, url)

    try:
      response = self.__session.get(url, params=kwargs)
      rep = Response(response, timer)
      if self.__debug:
        self.__logger.debug(rep)
      if rep.error:
        raise CoinMarketCapAPIError(rep)
      return rep
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      self.__logger.warning(e)
      raise e

  def cryptocurrency_info(self, **kwargs):
    return self.__get('{}/cryptocurrency/info'.format(self.__version), **kwargs)

  def cryptocurrency_map(self, **kwargs):
    return self.__get('{}/cryptocurrency/map'.format(self.__version), **kwargs)

  def cryptocurrency_listings_latest(self, **kwargs):
    return self.__get('{}/cryptocurrency/listings/latest'.format(self.__version), **kwargs)

  def cryptocurrency_market_pairs_latest(self, **kwargs):
    return self.__get('{}/cryptocurrency/market-pairs/latest'.format(self.__version), **kwargs)

  def cryptocurrency_ohlcv_historical(self, **kwargs):
    return self.__get('{}/cryptocurrency/ohlcv/historical'.format(self.__version), **kwargs)

  def cryptocurrency_quotes_latest(self, **kwargs):
    return self.__get('{}/cryptocurrency/quotes/latest'.format(self.__version), **kwargs)

  def cryptocurrency_quotes_historical(self, **kwargs):
    return self.__get('{}/cryptocurrency/quotes/historical'.format(self.__version), **kwargs)

  def exchange_info(self, **kwargs):
    return self.__get('{}/exchange/info'.format(self.__version), **kwargs)

  def exchange_map(self, **kwargs):
    return self.__get('{}/exchange/map'.format(self.__version), **kwargs)

  def exchange_listings_latest(self, **kwargs):
    return self.__get('{}/exchange/listings/latest'.format(self.__version), **kwargs)

  def exchange_market_pairs_latest(self, **kwargs):
    return self.__get('{}/exchange/market-pairs/latest'.format(self.__version), **kwargs)

  def exchange_quotes_latest(self, **kwargs):
    return self.__get('{}/exchange/quotes/latest'.format(self.__version), **kwargs)

  def exchange_quotes_historical(self, **kwargs):
    return self.__get('{}/exchange/quotes/historical'.format(self.__version), **kwargs)

  def global_metrics_quotes_latest(self, **kwargs):
    return self.__get('{}/global-metrics/quotes/latest'.format(self.__version), **kwargs)

  def global_metrics_quotes_historical(self, **kwargs):
    return self.__get('{}/global-metrics/quotes/historical'.format(self.__version), **kwargs)

  def tools_price_conversion(self, **kwargs):
    return self.__get('{}/tools/price-conversion'.format(self.__version), **kwargs)


