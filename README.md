# Cryptoscraper
## Brent Schillemans - 2 IMS

<br>

### Installatie VM - Ununtu
- Stap 1: .iso-file downloaden van officiële Ubuntu website
- Stap 2: virtuele machine opzetten via Oracle Virtual Box
- Stap 3: Ubuntu installeren en configureren
- Stap 4: python installeren, versie 3.8.10 reeds aanwezig
  > python3 --version
- Stap 5: python pakketten beautifulsoup en html5lib installeren
  > pip install beautifulsoup4 <br> pip install html5lib

<br> 

### Werking Crpytoscraper
Eens de python-file aan het lopen is, gaat deze automatisch elke minuut de data scrapen en in een json-file genaamd "scrapings.json" bewaren.
1. Scraper gaat via request naar "https://www.blockchain.com/btc/unconfirmed-transactions" de data ophalen
2. Even checken of json-file om data in te bewaren al bestaat of niet. Zo niet, deze aanmaken
3. De gescrapte data filteren, enkel de transacties, bestaande uit Hash, Time, Amount (BTC) en Amount (USD), hebben we nodig. Dit kan dankzij het pakket beautifulsoup, we zoeken hierbij in de html-structuur naar de klasse "sc-1g6z4xm-0 hXyplo"
4. De reeds gescrapte data wordt samengevoegd met de nieuwe data en gestored in de json-file
5. Na één minuut wordt het programma opnieuw gerunned en wordt nieuwe data gescraped