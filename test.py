import requests

URL = "https://api.coinbase.com/v2/prices/BTC-EUR/spot"

response = requests.get(URL)

print(response.text)