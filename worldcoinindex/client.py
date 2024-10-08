import requests
from datetime import datetime

class CryptocoinEngine:
  """
  Wrapper for the WorldCoinIndex API.
  """

  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "https://www.worldcoinindex.com/apiservice/"

  def _make_request(self, url, params=None):
    """
    Makes a GET request to the WorldCoinIndex API.
    """
    headers = {"X-API-Key": self.api_key}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise exception for non-200 status codes
    return response.json()

  def get_tickers(self, labels):
    """
    Fetches ticker data for specified labels.
    """
    url = f"{self.base_url}ticker?key={self.api_key}&label={labels}"
    data = self._make_request(url)
    return {item["Label"]: item for item in data["Markets"]}

  def get_markets(self, v2=False, fiat="btc"):
    """
    Fetches market data for all currencies.
    """
    endpoint = "v2getmarkets" if v2 else "getmarkets"
    url = f"{self.base_url}{endpoint}?key={self.api_key}&fiat={fiat}"
    data = self._make_request(url)
    for item in data["Markets"]:
      item["Timestamp"] = datetime.fromtimestamp(item["Timestamp"])
    return data["Markets"]
