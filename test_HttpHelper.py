import HttpHelper

def test_forex_to_hkd():
    res = HttpHelper.forex_to_hkd()
    for k in ["cad", "gbp", "usd", "eur"]:
        # Make sure key exists
        assert k in res
        # Make sure the value is correct
        assert float(res[k])
    assert isinstance(res, dict)

    # Check if global variable is updated
    # _valueForex is a cached
    assert HttpHelper._valueForex is not None

    # Check if global variable is updated
    # _lastForex is the timestamp of last poll
    # assert HttpHelper._lastForex is not None

    # Store the timestamp
    last_time_stamp = HttpHelper._lastForex

    # Store a copy of result
    last_res = res

    # If we call this function within 300 second, it should reuse cached result
    # Timestamp is not updated
    res = HttpHelper.forex_to_hkd()
    assert last_time_stamp == HttpHelper._lastForex
    assert last_res == res

def test_covid_cases():
    res = HttpHelper.covid_cases()
    assert isinstance(res, dict)
