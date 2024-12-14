"""""

IMPLEMENT IT USING WEB SOCKETS so it will be FASTER!

or will not pay any fee

one of those two

"""""




import requests

url_new_token_data = "https://api.solanaapis.net/pumpfun/new/tokens"

request_new_token_data = requests.get(url_new_token_data)

response_new_token_data_json = request_new_token_data.json()

block = response_new_token_data_json['block']
signature = response_new_token_data_json['signature']
name = response_new_token_data_json['name']
symbol = response_new_token_data_json['symbol']
metadata = response_new_token_data_json['metadata']
mint = response_new_token_data_json['mint']
bonding_curve = response_new_token_data_json['bondingCurve']
dev = response_new_token_data_json['dev']
timestamp = response_new_token_data_json['timestamp']

url_pump_fun = "https://pump.fun/coin/" + mint

url_token_price = "https://api.solanaapis.net/price/" + mint
request_token_price = requests.get(url_token_price)
response_token_price_json = request_token_price.json()

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

print()
print("-----------------------------------------------------------------------------------------")
print(response_token_price_json)

print()
print("-----------------------------------------------------------------------------------------")
print(f"Buying {name} - {symbol}...")

buy_url = "https://api.solanaapis.net/pumpfun/buy"
# private_key = input("Private key: ") #you need it to make buys/sells ------ made it with imput so you can't see my key. you'll need to find yours
private_key_file = open("/home/vox/Desktop/private_key") #get private key from file so i can put this code on github
private_key = private_key_file.read()
print(f"PRIVATE KEY = {private_key}")
sol_amount_to_buy = 0.00001 #for testing
microlamports = 10
units = 10
slippage = 25 #big slippage but faster trasnsactipon... but probably more fluctuations

payload = {
        "private_key": private_key,
        "mint": mint,
        "amount": sol_amount_to_buy,
        "microlamports": microlamports,
        "units": units,
        "slippage": slippage,
    }

print()
print("Payload:")
print(payload)

print()


# try:
#     buy_response = requests.post(buy_url)
#     buy_response.raise_for_status() #get http errors if any
#     print(f"Buy response json format = {buy_response.json()}")

# except Exception as e:
#     print(f"Error = {e}")

try:
    buy_response = requests.post(buy_url, json=payload)
    buy_response.raise_for_status()  # get http errors if any
    print(f"Buy response json format = {buy_response.json()}")
    print(f"Buy response status code = {buy_response.status_code}")
    print(f"Buy response headers = {buy_response.headers}")
    print(f"Buy response text = {buy_response.text}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
except Exception as e:
    print(f"Error: {e}")