
# Python-CoinMarketCap API Wrapper

This is a non official (but working) Python package to wrap the CoinMarketCap API. With this you can monitoring and watch the crypto market.

- First, you have to create an API on the [Developper Portal](https://coinmarketcap.com/api/)
- Read the official [API documentation](https://coinmarketcap.com/api/documentation/v1/)

[![Downloads](https://pepy.tech/badge/python-coinmarketcap/week)](https://pepy.tech/project/python-coinmarketcap)

---

## Installation

__Via pip__

- pip install __python-coinmarketcap__

> /!\ *Don't confound with the coinmarketcap package.*

## Example

```python

  from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

  cmc = CoinMarketCapAPI('{YOUR_API_KEY}')
  
  r = cmc.cryptocurrency_info(symbol='BTC')

  do_something(r.data)
```

---

## Wrapper References

### CoinMarketCapAPI

__Synopsis__

```
CoinMarketCapAPI(api_key=None, [debug=False, logger=None, sandbox=False, version='v1'])
```

- `debug`: set verbosity.
- `sandbox`: In case of default sandbox API key changes, see [Issue #1](https://github.com/rsz44/python-coinmarketcap/issues/1).
- `logger`: you can give a custom logger.
- `version`: set the version in the URL, for futures version.

__Methods__

You have to pass to following methods the parameters detailled in the [official documentation](https://coinmarketcap.com/api/documentation/v1/).

| Methods and documentation | Description | Endpoint |
|-|-|-|
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap)) __cryptocurrency_map__ | CoinMarketCap ID map | /cryptocurrency/map |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo)) __cryptocurrency_info__ | Metadata | /cryptocurrency/info |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest)) __cryptocurrency_listings_latest__ | Latest listings | /cryptocurrency/listings/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical)) __cryptocurrency_listings_historical__ | Historical listings | /cryptocurrency/listings/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest)) __cryptocurrency_quotes_latest__ | Latest quotes | /cryptocurrency/quotes/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesHistorical)) __cryptocurrency_quotes_historical__ | Historical quotes | /cryptocurrency/quotes/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest)) __cryptocurrency_marketpairs_latest__ | Latest market pairs | /cryptocurrency/market-pairs/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvLatest)) __cryptocurrency_ohlcv_latest__ | Latest OHLCV | /cryptocurrency/ohlcv/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvHistorical)) __cryptocurrency_ohlcv_historical__ | Historical OHLCV | /cryptocurrency/ohlcv/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyPriceperformancestatsLatest)) __cryptocurrency_priceperformancestats_latest__ | Price performance Stats | /cryptocurrency/price-performance-stats/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategories)) __cryptocurrency_categories__ | Categories | /cryptocurrency/categories |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory)) __cryptocurrency_category__ | Category | /cryptocurrency/category |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrops)) __cryptocurrency_airdrops__ | Airdrops | /cryptocurrency/airdrops |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrop)) __cryptocurrency_airdrop__ | Airdrop | /cryptocurrency/airdrop |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingLatest)) __cryptocurrency_trending_latest__ | Trending Latest | /cryptocurrency/trending/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingMostvisited)) __cryptocurrency_trending_mostvisited__ | Trending Most Visited | /cryptocurrency/trending/most-visited |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingGainerslosers)) __cryptocurrency_trending_gainerslosers__ | Trending Gainers & Losers | /cryptocurrency/trending/gainers-losers |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMap)) __exchange_map__ | CoinMarketCap ID map | /exchange/map |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo)) __exchange_info__ | Metadata | /exchange/info |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsLatest)) __exchange_listings_latest__ | Latest listings | /exchange/listings/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsHistorical)) __exchange_listings_historical__ | Historical listings | /exchange/listings/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesLatest)) __exchange_quotes_latest__ | Latest quotes | /exchange/quotes/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesHistorical)) __exchange_quotes_historical__ | Historical quotes | /exchange/quotes/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest)) __exchange_marketpairs_latest__ | Latest market pairs | /exchange/market-pairs/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest)) __globalmetrics_quotes_latest__ | Latest global metrics | /global-metrics/quotes/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical)) __globalmetrics_quotes_historical__ | Historical global metrics | /global-metrics/quotes/historical |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion)) __tools_priceconversion__ | Price conversion tool | /tools/price-conversion |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1BlockchainStatisticsLatest)) __blockchain_statistics_latest__ | Latest statistics | /blockchain/statistics/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap)) __fiat_map__ | CoinMarketCap ID map | /fiat/map |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasListingsLatest)) __partners_flipsidecrypto_fcas_listings_latest__ | List all available FCAS scores | /partners/flipside-crypto/fcas/listings/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasQuotesLatest)) __partners_flipsidecrypto_fcas_quotes_latest__ | Request specific FCAS scores | /partners/flipside-crypto/fcas/quotes/latest |
| ([doc](https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo)) __key_info__ | Key Info | /key/info |

__Additionnal Parameters__

- `api_version` (str): if given, will fetch the given version of the endpoint (default is equal to the given version in the CoinMarketCapAPI instance wich is actually `v1`).

__Example__

Assuming you want to get informations about bitcoin. First, read the [documentation]((https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo)) of the corresponding __cryptocurrency_info__ endpoint. 
  - You can pass the `symbol` parameter like : `cmc.cryptocurrency_info(symbol='BTC')`
  - or with the `slug` parameter : `cmc.cryptocurrency_info(slug='bitcoin')`

You can switch easly in the __sandbox mode__ without giving an API key or by setting it to `None` :
  - `cmc = CoinMarketCapAPI() # You are in sandbox environnement`

You can enable a __debuging mode__, just set `debug` to `True` to main class:

```python
  cmc = CoinMarketCapAPI(debug=True)
  cmc.cryptocurrency_info(symbol='BTC')
```

This will produce this output :

```
 2019-04-06 16:03:04,716 root         DEBUG    GET SANDBOX 'v1/cryptocurrency/info'
PARAMETERS: {'symbol': 'BTC'}
2019-04-06 16:03:05,004 root         DEBUG    RESPONSE: 288ms OK: {u'BTC': {u'category': u'coin', u'name': u'Bitcoin', u'tags': [u'mineable'], u'symbol': u'BTC', u'id': 1, [...]}
```


Optionnaly, you can pass (on-the-fly) a __specific version__ of an endpoint by given the `api_version` keyword argument directly to a method:
```python
cmc.cryptocurrency_listings_latest(..., api_version="v1.1")
```

__See also__
- [Quick Start Guide](https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide)

### Response

__Synopsis__

You get results of the API in a `Response` instance. 

__Property__

Corresponding to [standards and conventions](https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions):

- `data` (__dict__): will give you the result.
- `status` (__dict__): the status object always included for both successful calls and failures.
- `credit_count` (__int__): the number of credits this call utilized.
- `elapsed` (__int__):  the number of milliseconds it took to process the request to the server.
- `total_elapsed` (__int__): the total number of milliseconds it took to process the request.
- `timesamp` (__str__): current time on the server when the call was executed.
- `error_code` (__str | None__): In case of an error has been raised, this property will give you the status error code.
- `error_message` (__str | None__): In case of an error has been raised, this property will give details about error.
- `error` (__bool__): True if an error has been raised.

__Example__

```python
r = cmc.cryptocurrency_info(symbol='BTC')
print(repr(r.status))
print(repr(r.data))
print(repr(r.credit_count))
```

### CoinMarketCapAPIError

__Synopsis__

If API returns an error, `CoinMarketCapAPI` will raise a `CoinMarketCapAPIError`.

__Property__

- `rep` (__Response | None__): will give you a `Response` instance or `None` if request failed for an other reason than a server error.

__Example__

```python

  from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

  cmc = CoinMarketCapAPI('{YOUR_API_KEY}') # Pro environnement
  # cmc = CoinMarketCapAPI() # Sandbox environnement

  try:
    r = cmc.cryptocurrency_info(symbol='BTC')
  except CoinMarketCapAPIError as e:
    r = e.rep

  print(repr(r.error))
  print(repr(r.status))
  print(repr(r.data))

```

---

## See this project on

- [PyPi](https://pypi.org/project/python-coinmarketcap/)
- [Github](https://github.com/rsz44/python-coinmarketcap)

## ToDo

- [ ] Add Cryptocurrency Abstraction
- [ ] Add Exchange Abstraction
- [ ] Add GlobalMetrics Abstraction
- [ ] Add Tools Abstraction

## ChangeLog

- 31 aug 2021: Version 0.3
  - Adding new endpoints (Aug 17):
    + /v1/cryptocurrency/categories
    + /v1/cryptocurrency/category
    + /v1/cryptocurrency/airdrops
    + /v1/cryptocurrency/airdrop
    + /v1/cryptocurrency/trending/latest
    + /v1/cryptocurrency/trending/most-visited
    + /v1/cryptocurrency/trending/gainers-losers
  - PEP 8 style
  - Adding `api_version` keyword argument to all endpoints to change on-the-fly the api version to use.
- 8 sept 2020: Version 0.2
  - Adding missing endpoints
  - Fixing sandbox mode (see [Issue #1](https://github.com/rsz44/python-coinmarketcap/issues/1))
  - Adding `deflate, gzip` encoding to receive data fast and efficiently.
  - Documentation: adding usefull links
- 6 apr 2019: Version 0.1

## Give me a coffee

```
  BTC: 39aosiow4nsUvYVA2kP1hZPNZ7ZbJ6ouKr
  ETH: 0x45d940FDA3F1Ce91cA7CB478af72170bb6560201
```