import requests, json
from time import sleep
from bs4 import BeautifulSoup
from os.path import exists
from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('superuser')
password = urllib.parse.quote_plus('p@ss')

client = MongoClient("mongodb://%s:%s@127.0.0.1:27017" % (username,password))
db = client.cryptoscraper
collection = db.transaction

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

            ## wegschrijven naar DB
            newData = {hash:{"Time":time,"Amount (BTC)":amount_btc,"Amount (USD)":amount_usd}}
            collection.insert_one(newData)


    print("Programma uitgevoerd!")

    #Loop elke minuut
    sleep(60)