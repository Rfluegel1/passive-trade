import urllib.request
import json


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    with open('AVApiKey.txt', 'r') as apiKey:
        API_KEY = apiKey.readline()

    TIME_SERIES_INTRADAY = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=VOO&interval=5min' \
                           '&apikey=' + API_KEY

    with urllib.request.urlopen(TIME_SERIES_INTRADAY) as response:
        data = json.load(response)

    print(data)
    print_hi('PyCharm')
