import requests
from time import sleep
from bs4 import BeautifulSoup
import redis
from datetime import timedelta
from datetime import datetime

## Redis
r = redis.Redis(
    host="localhost",
    port=8081
)

while True:

    ## data ophalen
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"

    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="html5lib")

    ## data selecteren
    if soup.find("div", class_="sc-1g6z4xm-0 hXyplo") != None:
        list = soup.findAll("div", class_="sc-1g6z4xm-0 hXyplo")

        ## data formateren
        for item in list:
            item = str(item.get_text())

            hash = item.replace("Hash","").split("Time")[0]
            time = item.split("Time")[1].split("Amount (BTC)")[0]
            amount_btc = item.split("Amount (BTC)")[1].split("Amount (USD)")[0]
            amount_usd = item.split("Amount (BTC)")[1].split("Amount (USD)")[1]

            newData = {"Hash":hash,"Time":time,"Amount (BTC)":amount_btc,"Amount (USD)":amount_usd}

            ## transacties toevoegen aan cache en bijhouden voor 60 seconden
            r.hmset(hash, newData)
            r.expire(hash, timedelta(seconds=60))

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Programma uitgevoerd! -",current_time)

    #Loop elke minuut
    sleep(60)
