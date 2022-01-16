import collections
import requests
import json



url = "https://api.opensea.io/api/v1/collections?asset_owner=0x780da7b4fba0320ba745eb584e7955694ad90f7e&owner=0x780da7b4fba0320ba745eb584e7955694ad90f7e"


headers = {"Accept": "application/json"}


response = requests.request("GET", url, headers=headers)

jsonDictionary = json.loads(response.text)

for item in jsonDictionary['collections']:
    print (item['slug'])


#print(response.text)