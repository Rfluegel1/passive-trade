import urllib.request
import json

USE_LOCAL_JSON = True


def getApiKey():
    with open('AVApiKey.txt', 'r') as apiKey:
        return apiKey.readline()


def getAlphaVantageURL(function='TIME_SERIES_INTRADAY', symbol='VOO', interval='5'):
    return 'https://www.alphavantage.co/query?function=' + function + \
           '&symbol=' + symbol + \
           '&interval=' + interval + \
           'min&apikey=' + getApiKey()


def getData(url=getAlphaVantageURL()):
    if USE_LOCAL_JSON:
        with open('VOO.json') as VOOJson:
            return json.load(VOOJson)
    else:
        with urllib.request.urlopen(url) as response:
            return json.load(response)


if __name__ == '__main__':
    print(getData())
