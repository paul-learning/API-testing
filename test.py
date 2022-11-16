import requests


def get_bitcoin():
    URL = "https://api.coinbase.com/v2/prices/BTC-EUR/spot"
    response = requests.get(URL)
    return(response.text)

print(get_bitcoin())