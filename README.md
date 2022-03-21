# Cryptoscraper
## Brent Schillemans - 2 IMS

<br>

### Installatie VM - Ubuntu
- Stap 1: .iso-file downloaden van officiële Ubuntu website
- Stap 2: virtuele machine opzetten via Oracle Virtual Box
- Stap 3: Ubuntu installeren en configureren
- Stap 4: python installeren, versie 3.8.10 reeds aanwezig
  > python3 --version
- Stap 5: python pakketten beautifulsoup en html5lib installeren
  > pip install beautifulsoup4 <br> pip install html5lib

<br> 

### Werking Crpytoscraper
Eens de python-file aan het lopen is, gaat deze automatisch elke minuut de data scrapen. Er wordt gekeken in Redis, het caching-mechanisme, of de hash reeds bestaat en dus in de datebase zou zitten. Zo niet wordt deze in de collectie "transaction" van de database "cryptoscraper" op MongoDB opgeslagen. De hash wordt voor 65 seconden in de cache opgeslagen zodat deze juist op tijd kan opgevraagd worden of het reeds bestaat of niet.
1. Scraper gaat via request naar "https://www.blockchain.com/btc/unconfirmed-transactions" de data ophalen
2. De gescrapte data filteren: enkel de transacties, bestaande uit Hash, Time, Amount (BTC) en Amount (USD), hebben we nodig. Dit kan dankzij het pakket beautifulsoup, we zoeken hierbij in de html-structuur naar de klasse "sc-1g6z4xm-0 hXyplo"
3. We gaan in Redis kijken of de hash reeds in de cache staat; zo niet wordt deze transactie bijgevoegd in de MongoDB databse
4. De hash wordt aan Redis toegevoegd voor 65 seconden zodat we juist op tijd (met marge gerekend) kunnen opvragen de volgende keer dat de scraper loopt of de gescrapte hashes reeds bestaan of niet
5. Na één minuut wordt het programma opnieuw gerunned en wordt nieuwe data gescraped
