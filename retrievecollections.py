import requests
import json


url = "https://api.opensea.io/api/v1/collections?asset_owner=0x83943171e9d102a238f87258fa40c3b79879f29e&owner=0x83943171e9d102a238f87258fa40c3b79879f29e"


headers = {"Accept": "application/json"}


response = requests.request("GET", url, headers=headers)

responseObject = json.loads(response.text)

for collectionsObject in responseObject.items():
    for collection in collectionsObject:
        print(collection)

    

#print(response.text)