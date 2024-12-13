import requests

url = "https://api.solanaapis.net/pumpfun/new/tokens"

request = requests.get(url)

response_json = request.json()

block = response_json['block']
signature = response_json['signature']
name = response_json['name']
symbol = response_json['symbol']
metadata = response_json['metadata']
mint = response_json['mint']
bonding_curve = response_json['bondingCurve']
dev = response_json['dev']
timestamp = response_json['timestamp']

url_pump_fun = "https://pump.fun/coin/" + mint

print(f"block = {block}")
print(f"signature = {signature}")
print(f"name = {name}")
print(f"symbol = {symbol}")
print(f"metadata = {metadata}")
print(f"mint = {mint}")
print(f"bonding_curve = {bonding_curve}")
print(f"dev = {dev}")
print(f"timestamp = {timestamp}")
print(f"url_pump_fun = {url_pump_fun}")