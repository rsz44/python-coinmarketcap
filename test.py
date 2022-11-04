from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import time
import logging

STOP_ON_ERROR = True
DEBUG = True

wrapper_methods = [
    "cryptocurrency_map",
    "cryptocurrency_info",
    "cryptocurrency_listings_latest",
    "cryptocurrency_listings_historical",
    "cryptocurrency_quotes_latest",
    "cryptocurrency_quotes_historical",
    "cryptocurrency_marketpairs_latest",
    "cryptocurrency_ohlcv_latest",
    "cryptocurrency_ohlcv_historical",
    "cryptocurrency_priceperformancestats_latest",
    "cryptocurrency_categories",
    "cryptocurrency_category",
    "cryptocurrency_airdrops",
    "cryptocurrency_airdrop",
    "cryptocurrency_trending_latest",
    "cryptocurrency_trending_mostvisited",
    "cryptocurrency_trending_gainerslosers",
    "exchange_map",
    "exchange_info",
    "exchange_listings_latest",
    "exchange_listings_historical",
    "exchange_quotes_latest",
    "exchange_quotes_historical",
    "exchange_marketpairs_latest",
    "globalmetrics_quotes_latest",
    "globalmetrics_quotes_historical",
    "tools_priceconversion",
    "tools_postman",
    "blockchain_statistics_latest",
    "fiat_map",
    "partners_flipsidecrypto_fcas_listings_latest",
    "partners_flipsidecrypto_fcas_quotes_latest",
    "key_info",
    "content_posts_top",
    "content_posts_latest",
    "content_posts_comments",
    "content_latest"
]

cmc = CoinMarketCapAPI(debug=True, logger=logging.getLogger(__name__)) # Sandbox

errors = []
passed = []

for method in wrapper_methods:

    try:
        getattr(cmc, method)
        passed.append(method)
    except CoinMarketCapAPIError as cmc_error:
        errors.append(method)
        if STOP_ON_ERROR:
            break

    time.sleep(0.1)


print(f"Passed : {len(passed)}/{len(wrapper_methods)}")
print(f"Errors : {len(errors)}/{len(wrapper_methods)}")
for err in errors:
    print(f"\t- {err}")

