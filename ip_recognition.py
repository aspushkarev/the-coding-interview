"""
Resolution your ip-address and region
"""
import json

import requests

url_1 = "https://api.ipify.org?format=json "
url_2 = "http://ip-api.com/json/"

# find ip
response = requests.get(url_1)
ip_address = response.text

# find extension information about ip
response = requests.get(url_2)
ip_json = response.text

# decoding JSON to dict
ip_dict = json.loads(ip_json)

print(f'Your ip-address is ', ip_address)
print(f'Your region is ', ip_dict['region'])
