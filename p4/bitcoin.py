import sys
import json
import requests

if len(sys.argv) < 2:
    print("Missing cmd-line arg")
    sys.exit()
else:
    try:
        user_input = float(sys.argv[1])
    except ValueError:
        print("Not a number")
        sys.exit()

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print("Request Error")
else:
    o = response.json()
    rate = o["bpi"]["USD"]["rate_float"]
    print(f"${round(rate * user_input, 4):,.4f}")