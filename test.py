import sys
import os
import time
import logging

# == TESTS CONFIG ==
DEBUG = True
STOP_ON_ERROR = True
WRAPPER_METHODS = [
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
    "content_latest",
    "exchange_assets",
    "community_trending_token",
    "community_trending_topic",
    "fearandgreed_latest",
    "fearandgreed_historical",
]
KNOWN_TESTS_500 = [
    # v3 endpoints in sandbox returns 500 on Jan. 2025
    "fearandgreed_latest",
    "fearandgreed_historical",
]
# == *END OF* TESTS CONFIG ==

try:
    from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
    IMPORT_ERROR = False
except ImportError as import_error:
    IMPORT_ERROR = import_error

def _debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def exitOnFailed(_test, msg="Last test failed."):
    if bool(_test) and STOP_ON_ERROR:
        _debug(msg)
        _debug("Failed, *exit*")
        sys.exit(1)

def check_members(cmc_instance):

    _objectBaseMeth = dir(object()) + ['__dict__', '__module__', '__weakref__']
    _cmcKnownMembers = ['__base_url', '__debug', '__get', '__headers', '__key', '__logger', '__sandbox', '__session', '__version']
    _cmcKnownMembers = [f"_{cmc_instance.__class__.__name__}{km}" for km in _cmcKnownMembers]
    unknownMembers = []

    for _mb in dir(cmc_instance):
        known_member = (_mb in _cmcKnownMembers)
        base_member = (_mb in _objectBaseMeth)
        tested_member = (_mb in WRAPPER_METHODS)

        if any([known_member, base_member, tested_member]):
            continue
        else:
            _debug(f"Error: Unknown or undefined test method for '{_mb}' in CoinMarketCapAPI instance.")
            unknownMembers.append(_mb)
            if not known_member and _mb.startswith("_CoinMarketCapAPI"):
                _debug(f"Error: Unknown private member '{_mb[17:]}'.")
            else:
                _debug(f"Error: Undefined test method for member '{_mb}'.")

            if STOP_ON_ERROR:
                break

    _unknownTest = []
    for test_method in WRAPPER_METHODS:
        try:
            _boundmethod = getattr(cmc_instance, test_method)
        except AttributeError:
            _unknownTest.append(test_method)
            _debug(f"Error: no corresponding member for test '{test_method}'")
            if STOP_ON_ERROR:
                break
    return (len(unknownMembers) != 0) or (len(_unknownTest) != 0)

def check_method(cmc_instance, method, send_request=True):

    try:
        bound_method = getattr(cmc_instance, method)
    except AttributeError:
        _debug(f"'{method}' is not attribute of `cmc` instance.")
        return False

    if not send_request:
        return False

    try:
        rep = bound_method() # (*)unknown argument for methods (leave empty here).
        if not (rep._req.status_code in [200, 400, 500]):
            # (*)This test considering 400 (Bad resquest) as Ok.
            # As defined in 'Standards and Conventions'
            #   400 (Bad Request) The server could not process the request, 
            #   likely due to an invalid argument.
            _debug(f"Response status_code must be 200 or 400 or 500, got {rep._req.status_code}")
            return True

    except CoinMarketCapAPIError as _error:
        if _error.rep._req.status_code == 400:
            # consiering OK.
            pass
        elif _error.rep._req.status_code == 500 and method in KNOWN_TESTS_500:
            # consiering OK.
            _debug(f"(ignored) CoinMarketCapAPIError known 500 for '{method}'.")
            pass
        else:
            _debug(f"CoinMarketCapAPIError raised while testing '{method}':\n\t-> {_error.rep}.")
            return True
    except Exception as _error:
        _debug(f"Unexpected '{_error.__class__.__name__}' raised while testing '{method}':\n\t-> {repr(_error)}.")
        return True
    return False

def check_all_methods(cmc_instance, send_request=True):
    errors = []
    passed = []

    for method in WRAPPER_METHODS:  
        _fail = check_method(cmc_instance, method, send_request)
        exitOnFailed(_fail, f'Error while testing method "{method}"')    
        if _fail:
            errors.append(method)
        else:
            passed.append(method)
        time.sleep(0.1)

    _debug(f"Passed : {len(passed)}/{len(WRAPPER_METHODS)}")
    _debug(f"Errors : {len(errors)}/{len(WRAPPER_METHODS)}")
    for err in errors:
        _debug(f"\t- {err}")
    return (len(errors) != 0)

def check_codestyle():
    if not DEBUG:
        return
    try:
        import pycodestyle
    except ImportError:
        _debug(f"Missing `pycodestyle` package (install via `pip install pycodestyle)` to check PEP8.")
        return

    fpath = os.path.join(os.path.join(os.path.dirname(__file__), "coinmarketcapapi"), "__init__.py")
    fchecker = pycodestyle.Checker(fpath, show_source=True)
    file_errors = fchecker.check_all()
    _debug(f"Code Style : Found {file_errors} errors (and warnings)")
    return (file_errors != 0)




def test_all(cmc_instance=None, send_request=True):
    exitOnFailed( (IMPORT_ERROR is not False), f"Error while importing CoinMarketCapAPI, CoinMarketCapAPIError : {repr(IMPORT_ERROR)}.")

    if cmc_instance is not None:
        assert isinstance(cmc_instance, CoinMarketCapAPI), "Expected a CoinMarketCapAPI instance to test as `cmc_instance`."
        cmc = cmc_instance
    else:
        cmc = CoinMarketCapAPI(debug=True, logger=logging.getLogger(__name__)) # Sandbox

    exitOnFailed( check_members(cmc), f"Error while testing Instance members.")
    exitOnFailed( check_all_methods(cmc, send_request=send_request), f"Error while testing wrapped method" )
    exitOnFailed( check_codestyle(), "Error on code style.")

if __name__ == "__main__":
    test_all()
