from worldcoinindex import CryptocoinEngine
import os

API_KEY = os.environ.get("WCI_API_KEY")
engine = CryptocoinEngine(api_key=API_KEY)


def test_tickers():
    response = engine.get_tickers(labels=["ethbtc"], fiat="USD")

    assert isinstance(response, dict)


def test_markets():
    response = engine.get_markets(fiat="USD")

    assert isinstance(response, dict)
