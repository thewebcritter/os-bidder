import requests
import json

class Asset:
    test = True
    asset = dict
    
    # object information


    def __init__(self):
        self.data = []

    def loadAsset(self,assetDictionary):
        print ("Loading Asset from Dictionary section")
        asset = assetDictionary
        print (asset['id'])



url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&collection=azurobet-nft-zc5svhbywu"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
jsonDictionary = json.loads(response.text)
a1 = Asset()
for asset in jsonDictionary['assets']:    
    a1.loadAsset(asset)
    print (a1.test)