from time import sleep
from pymongo import MongoClient
import redis
from datetime import datetime

## mongoDB
client = MongoClient("mongodb://127.0.0.1:8080")
db = client.cryptoscraper
collection = db.transaction

## Redis
r = redis.Redis(
    host="localhost",
    port=8081
)

while True:

    maxHash = ""
    maxValue = 0
    maxString = {}

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
    
    if collection.find_one(maxString) == None:
        collection.insert_one(maxString)
    
    print("Grootste hash:",maxHash,"met waarde $",maxValue)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Programma uitgevoerd! -",current_time)

    #Loop elke minuut
    sleep(60)