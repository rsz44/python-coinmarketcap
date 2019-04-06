# Python-CoinMarketCap API Wrapper

This is a non official (but working) Python package to wrap the CoinMarketCap API.

With this you can monitoring and watch the crypto market.

## Installation

### Via pip

- pip install __python-coinmarketcap__

/!\ *Don't confound with the coinmarketcap package.*

### Manual Installation

Clone this repo and  :


## Example

```python

  import coinmarketcapapi

  cmc = CoinMarketCapAPI('{YOUR_API_KEY}')
  r = cmc.cryptocurrency_info(symbol='BTC')
  
  print repr(r.data)
  
```

## Requirements and links

First, you have to create an API on the Developper Portal : https://coinmarketcap.com/api/

You can found the full official documentation here : https://coinmarketcap.com/api/documentation/v1/


## API Guide

### List of all methods

You have to pass to theses functions the parameters detailled in the official documentation.

Endoints :

- __cryptocurrency_info__: Get cryptocurrency metadata
- __cryptocurrency_map__: Get cryptocurrency CoinMarketCap ID map
- __cryptocurrency_listings_latest__: List all cryptocurrencies (latest)
- __cryptocurrency_market_pairs_latest__: Get cryptocurrency market pairs (latest)
- __cryptocurrency_ohlcv_historical__: Get cryptocurrency OHLCV values (historical)
- __cryptocurrency_quotes_latest__: Get cryptocurrency market quotes (latest)
- __cryptocurrency_quotes_historical__: Get cryptocurrency market quotes (historical)
- __exchange_info__: Get exchange metadata
- __exchange_map__: Get exchange to CoinMarketCap ID map
- __exchange_listings_latest__: List all exchanges (latest)
- __exchange_market_pairs_latest__: Get exchange market pairs (latest)
- __exchange_quotes_latest__: Get exchange market quotes (latest)
- __exchange_quotes_historical__: Get exchange market quotes (historical)
- __global_metrics_quotes_latest__: Get aggregate market metrics (latest)
- __global_metrics_quotes_historical__: Get aggregate market metrics (historical)
- __tools_price_conversion__: Price conversion tool

### Response

Just get the results of the API in `rep.data` or check the status with `rep.status`.

### Sanbox / Pro Environement

You can switch easly you have to set `sandbox` the default value is `True`.

```python
  cmc = CoinMarketCapAPI('{YOUR_API_KEY}', sandbox=False)
  # You are in production environnement
```

### Debuging

You can enable a debuging mode, just set `debug` to `True` to main class:

```python
  cmc = CoinMarketCapAPI('{YOUR_API_KEY}', debug=True)
```

Will produce a new output :

```
 2019-04-06 16:03:04,716 root         DEBUG    GET SANDBOX 'v1/cryptocurrency/info'
PARAMETERS: {'symbol': 'BTC'}
2019-04-06 16:03:05,004 root         DEBUG    RESPONSE: 288ms OK: {u'BTC': {u'category': u'coin', u'name': u'Bitcoin', u'tags': [u'mineable'], u'symbol': u'BTC', u'id': 1, [...]}
```

You can also passing directly a logger instance :


```python
  cmc = CoinMarketCapAPI('{YOUR_API_KEY}', debug=True, logger=my_logger)
```

## ToDo

- [ ] Add Cryptocurrency Abstraction
- [ ] Add Exchange Abstraction
- [ ] Add GlobalMetrics Abstraction
- [ ] Add Tools Abstraction

## ChangeLog

- 6 apr 2019: Version 0.1