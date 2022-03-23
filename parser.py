import requests, json
from time import sleep
from bs4 import BeautifulSoup
from os.path import exists
from pymongo import MongoClient
import urllib.parse
import redis

## mongoDB
client = MongoClient("mongodb://127.0.0.1:8080")
db = client.cryptoscraper
collection = db.transaction

## Redis
r = redis.Redis(
    host="localhost",
    port=8081
)

maxHash = ""
maxValue = 0
maxString = {}

while True:

    ## data ophalen uit Redis
    for key in r.keys():
        key = str(key).split("'")[1]
        value = r.hgetall(key)
        value = str(value).split("'")

        hash = value[3]
        time = value[7]
        btc = value[11]
        usd = value[15]
        usdValue = float(usd.replace("$","").replace(",","",-1))

        if usdValue > maxValue:
            maxHash = hash
            maxValue = usdValue

            maxString = {hash:{"Time":time,"Amount (BTC)":btc,"Amount (USD)":usd}}
                

        print(key,"-",time,"-",btc,"-",usd)
        print()

    collection.insert_one(maxString)
    print("Grootste hash:",maxHash,"met waarde $",maxValue)
    print("Programma uitgevoerd!")

    #Loop elke minuut
    sleep(60)