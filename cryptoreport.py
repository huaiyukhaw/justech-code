# pip install requests
# pip install beautifulsoup4

import requests, bs4, csv, re

res = requests.get("https://cryptoreport.com/all")

crypto_report = bs4.BeautifulSoup(res.text, "html.parser")

elems = crypto_report.select('td')

i = 0
coins = []
coin = []

for elem in elems:
    if i == 1:
        i += 1
        continue

    if i != 7:
        coin.append(re.sub('[$,%]','',elem.get_text()))
        i += 1
        continue
    
    if i == 7:
        coin.append(re.sub('[$,%]','',elem.get_text()))
        coins.append(coin)
        i = 0
        coin = []
        continue

with open("crypto.csv", "w", newline='') as f:
    output_writer = csv.writer(f)
    output_writer.writerow(["No.", "Name", "Symbol", "Price ($)", "Change (%)", "Market Cap ($)", "24 Hour Volume ($)"])

    for coin in coins:
        output_writer.writerow(coin)


    