import requests
import json

collectionslug = "tenshi-girl"
headers = {"Accept": "application/json"}

url = "https://testnets-api.opensea.io/api/v1/collection/"+collectionslug
print ("URL : ",url)
response = requests.request("GET", url, headers=headers)
collectionDict = json.loads(response.text)


print ("Summary of Colleciton")
print ("=====================")
print ("* Collection Name : ",collectionDict['collection']['name'])
print ("* Collection Asset Count : ",collectionDict['collection']['stats']['count'])
print ("* Collection Floor : ",collectionDict['collection']['stats']['floor_price'])
print ("* Primary asset contracts : ",collectionDict['collection']['primary_asset_contracts'][0]['address'])
print ("** STATS **")
print ("** 1 Day Sales : ",collectionDict['collection']['stats']['one_day_sales'])
print ("** 1 Day Volume : ",collectionDict['collection']['stats']['one_day_volume'])
print ("** 1 Day AVG Price : ",collectionDict['collection']['stats']['one_day_average_price'])
print ("** 7 Day Sales : ",collectionDict['collection']['stats']['seven_day_sales'])
print ("** 7 Day Volume : ",collectionDict['collection']['stats']['seven_day_volume'])
print ("** 7 Day AVG Price : ",collectionDict['collection']['stats']['seven_day_average_price'])
print ('***********')

url = "https://testnets-api.opensea.io/api/v1/assets?collection="+collectionslug
print ("URL : ",url)
response = requests.request("GET", url, headers=headers)
jsonDictionary = json.loads(response.text)

for asset in jsonDictionary['assets']:   
    print ("Asset ID : ",asset['id'])
    print ("Asset Token ID : ",asset['token_id'])
    if(asset['last_sale'] is not None):
        print ("Last Sale(ETH) : ",asset['last_sale']['payment_token']['eth_price'])
        print ("Last Sale(ETH) : ",asset['last_sale']['payment_token']['usd_price'])
    print ("Top Bid : ",asset['top_bid'])
    print ("Listing Date : ",asset['listing_date'])
    print ("Is Presale ? : ",asset['is_presale'])
    print ("Transfer Fee : ",asset['transfer_fee'])   
    #print ("Creator : ",asset['creator']['user'],"(",asset['creator']['address'],")")

#print (jsonDictionary['collection']['slug'])
 
    
#print(response.text)