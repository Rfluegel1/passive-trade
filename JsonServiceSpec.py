import unittest
import json

from JsonService import JsonService

with open('VOO.json') as VOOJsonFile:
    VOOJson = json.load(VOOJsonFile)


class TestJsonService(unittest.TestCase):
    def setUp(self):
        self.jsonService = JsonService()

    def test_initial_json(self):
        self.assertEqual(self.jsonService.json, '')

    def test_get_most_recent_data(self):
        self.maxDiff = None
        self.jsonService.json = VOOJson
        actualMostRecentData = self.jsonService.getMostRecentData()
        expectedMostRecentData = {
            "1. open": "358.0200",
            "2. high": "358.0200",
            "3. low": "357.8500",
            "4. close": "357.8800",
            "5. volume": "12932"
        }
        self.assertEqual(actualMostRecentData, expectedMostRecentData)
