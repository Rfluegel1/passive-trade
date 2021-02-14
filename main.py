import json
import urllib.request
from JsonService import JsonService
from JsonServiceSpec import TestJsonService

USE_LOCAL_JSON = True
RUN_TESTS = True


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


def testJsonService():
    testJsonService = TestJsonService()
    testJsonService.setUp()
    testJsonService.test_initial_json()
    testJsonService.test_get_data()


def runAllTests():
    testJsonService()


if __name__ == '__main__':
    if RUN_TESTS:
        runAllTests()
