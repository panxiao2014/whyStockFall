import requests

with open("../data/alpha.vantage.key.txt", "r") as f:
    API_KEY = f.read().strip()
url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_KEY}"

response = requests.get(url)
data = response.text

#save first and second columns of data to a csv file in data folder
with open("../data/tickers.csv", "w") as f:
    for line in data.splitlines():
        f.write(",".join(line.split(",")[:2]) + "\n")
