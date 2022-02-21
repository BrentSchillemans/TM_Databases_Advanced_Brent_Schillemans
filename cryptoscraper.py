import requests, json
from time import sleep
from bs4 import BeautifulSoup
from os.path import exists

while True:

    ## data ophalen
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"

    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="html5lib")
    
    ## bestaat json-file al?
    if exists("scrapings.json"):
        f = open("scrapings.json",'r')
        oldJson = f.read()
        f.close()
    else:
        f = open("scrapings.json",'w')
        oldJson = ""
        f.close()

    ## data selecteren
    if soup.find("div", class_="sc-1g6z4xm-0 hXyplo") != None:
        list = soup.findAll("div", class_="sc-1g6z4xm-0 hXyplo")
        newJson = ""

        ## data formateren
        for item in list:
            item = str(item.get_text())

            hash = item.replace("Hash","").split("Time")[0]
            time = item.split("Time")[1].split("Amount (BTC)")[0]
            amount_btc = item.split("Amount (BTC)")[1].split("Amount (USD)")[0]
            amount_usd = item.split("Amount (BTC)")[1].split("Amount (USD)")[1]

            newJson += ',{' + f'"Hash":"{hash}","Time":"{time}","Amount (BTC)":"{amount_btc}","Amount (USD)":"{amount_usd}"' + '}'

    ## wegschrijven naar file
    if oldJson == "":
        newJson = newJson.replace(",{","{",1)

    f = open("scrapings.json",'w')
    writeText = "[" + oldJson.replace('[','').replace(']','') + newJson + "]"
    f.write(writeText)
    f.close()

    print("Programma uitgevoerd!")

    #Loop elke minuut
    sleep(60)