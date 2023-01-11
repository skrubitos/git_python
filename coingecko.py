import requests


#bitcoin
def btc():

    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&api_key="
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    print(f"The current price of Bitcoin is ${price}.")
#ethereum
def eth():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&api_key="
    response = requests.get(url)
    data = response.json()
    price = data["ethereum"]["usd"]
    print(f"The current price of Ethereum is ${price}.")
#chainlink
def link():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd&api_key="
    response = requests.get(url)
    data = response.json()
    price = data["chainlink"]["usd"]
    print(f"The current price of Chainlink is ${price}.")
#polkadot
def dot():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd&api_key="
    response = requests.get(url)
    data = response.json()
    price = data["polkadot"]["usd"]
    print(f"The current price of Polkadot is ${price}.")


btc()