
# Python-CoinMarketCap API Wrapper

This is a non-official (but working) Python package to wrap the CoinMarketCap API. With this you can monitor and watch the crypto market.

- Read the official [API documentation](https://coinmarketcap.com/api/documentation/v1/)
- For the pro version, get an API Key on the [Developper Portal](https://coinmarketcap.com/api/)
- Be sure to replace the API Key in sample code with your own.

[![Downloads](https://pepy.tech/badge/python-coinmarketcap/week)](https://pepy.tech/project/python-coinmarketcap)

---

## Installation

```
pip install python-coinmarketcap
```

## Example

```python

from coinmarketcapapi import CoinMarketCapAPI

cmc = CoinMarketCapAPI()
  
rep = cmc.cryptocurrency_info(symbol='BTC') # See methods below

print(rep.data)                 # Whole repsonse payload
print(rep.data["BTC"]["logo"])  # Some data in response
print(rep.credit_count)         # API credits
print(rep.total_elapsed)        # Request time in ms
# ...

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

You have to pass to the following methods the parameters detailed in the [official documentation](https://coinmarketcap.com/api/documentation/v1/).

| Methods and 📄documentation | Endpoint (version) |
|-|-|
| [__cryptocurrency_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap) | /cryptocurrency/map |
| [__cryptocurrency_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyInfo) | /cryptocurrency/info (v2) |
| [__cryptocurrency_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) | /cryptocurrency/listings/latest |
| [__cryptocurrency_listings_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical) | /cryptocurrency/listings/historical |
| [__cryptocurrency_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest) | /cryptocurrency/quotes/latest (v2) |
| [__cryptocurrency_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesHistorical) | /cryptocurrency/quotes/historical (v2) |
| [__cryptocurrency_marketpairs_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyMarketpairsLatest) | /cryptocurrency/market-pairs/latest (v2) |
| [__cryptocurrency_ohlcv_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvLatest) | /cryptocurrency/ohlcv/latest (v2) |
| [__cryptocurrency_ohlcv_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical) | /cryptocurrency/ohlcv/historical (v2) |
| [__cryptocurrency_priceperformancestats_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyPriceperformancestatsLatest) | /cryptocurrency/price-performance-stats/latest (v2) |
| [__cryptocurrency_categories__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategories) | /cryptocurrency/categories |
| [__cryptocurrency_category__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory) | /cryptocurrency/category |
| [__cryptocurrency_airdrops__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrops) | /cryptocurrency/airdrops |
| [__cryptocurrency_airdrop__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrop) | /cryptocurrency/airdrop |
| [__cryptocurrency_trending_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingLatest) | /cryptocurrency/trending/latest |
| [__cryptocurrency_trending_mostvisited__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingMostvisited) | /cryptocurrency/trending/most-visited |
| [__cryptocurrency_trending_gainerslosers__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingGainerslosers) | /cryptocurrency/trending/gainers-losers |
| [__exchange_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMap) | /exchange/map |
| [__exchange_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo) | /exchange/info |
| [__exchange_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsLatest) | /exchange/listings/latest |
| [__exchange_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesLatest) | /exchange/quotes/latest |
| [__exchange_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesHistorical) | /exchange/quotes/historical |
| [__exchange_marketpairs_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest) | /exchange/market-pairs/latest |
| [__globalmetrics_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest) | /global-metrics/quotes/latest |
| [__globalmetrics_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical) | /global-metrics/quotes/historical |
| [__tools_priceconversion__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2ToolsPriceconversion) | /tools/price-conversion (v2) |
| [__tools_postman__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPostman) | /tools/postman |
| [__blockchain_statistics_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1BlockchainStatisticsLatest) | /blockchain/statistics/latest |
| [__fiat_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap) | /fiat/map |
| [__partners_flipsidecrypto_fcas_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasListingsLatest) | /partners/flipside-crypto/fcas/listings/latest |
| [__partners_flipsidecrypto_fcas_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasQuotesLatest) | /partners/flipside-crypto/fcas/quotes/latest |
| [__key_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo) | /key/info |
| [__content_posts_top__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsTop) | /content/posts/top |
| [__content_posts_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsLatest) | /content/posts/latest |
| [__content_posts_comments__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsComments) | /content/posts/comments |
| [__content_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentLatest) | /content/latest |
| [__fearandgreed_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV3FearandgreedLatest) | /fear-and-greed/latest (v3) |
| [__fearandgreed_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV3FearandgreedHistorical) | /fear-and-greed/historical (v3) |
| [__exchange_assets__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeAssets) | /exchange/assets |
| [__community_trending_token__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CommunityTrendingToken) | /community/trending/token |
| [__community_trending_topic__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CommunityTrendingTopic) | /community/trending/topic |

__Additionnal Parameters__

- `api_version` (str): if given, will fetch the given version of the endpoint (default is equal to the given version in the CoinMarketCapAPI instance wich is actually `v1`). As mentioned in the list above, some endpoints are "v2" by default.

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

## ChangeLog

- 25 jan 2025: Version 0.6
  - New endpoints (2.0.8, 2.0.9, 2.0.10):
    + /v3/fear-and-greed/latest
    + /v3/fear-and-greed/historical
    + /v1/community/trending/topic
    + /v1/community/trending/token
    + /v1/exchange/assets
  - Now handle `JSONDecodeError` as `CoinMarketCapAPIError`.
  - Removing 'exchange_listings_historical' method. Introduced in v0.2 (commit 6e3d605), there is no official trace of this endpoint and it doesn't seem to exist. This is probably a completion error when writing v0.2. If this endpoint is recognized, please open an issue.
  - Almost complete rewriting of `./test.py`.
  - No longer supported in Python 2.7
  - Miscellaneous README adjustments
- 4 nov 2022: Version 0.5
  - Remove an unfortunate debug that could display text unnecessarily during an error.
  - Yanked version 0.4
- 4 nov 2022: Version 0.4
  - Adding new endpoints (Aug 18/Sep 19):
    + /v1/content/posts/top
    + /v1/content/posts/latest
    + /v1/content/posts/comments
    + /v1/content/latest
    + /v1/tools/postman
      + This last one will clearly be useful to extend the wrapper according to the received schemes.
  - Fix `api_key` default to Sandbox mode.
  - Fix the logger, [Issue#4](https://github.com/rsz44/python-coinmarketcap/issues/4) from AlverGan.
  - Fix install_requires, requests was missing.
  - Changing the default API version to `v2` for some endpoints :
    + /v2/cryptocurrency/info
    + /v2/cryptocurrency/quotes/latest
    + /v2/cryptocurrency/quotes/historical
    + /v2/cryptocurrency/market-pairs/latest
    + /v2/cryptocurrency/ohlcv/latest
    + /v2/cryptocurrency/ohlcv/historical
    + /v2/cryptocurrency/price-performance-stats/latest
    + /v2/tools/price-conversion
  - On the Readme:
    + Adding new methods references.
    + Modification of the methods table to improve readability.
    + Some grammatical corrections in README (Thanks to [__@tactipus__](https://github.com/tactipus) !).
    + Small changes and removal of some unnecessary spaces in the example codes.
    + Adding reading references about the API and the package (Thanks to their respective authors !).
  - Adding docstring to classes.
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
