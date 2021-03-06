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

    def test_get_data(self):
        # Most recent
        self.jsonService.json = VOOJson
        actualMostRecentData = self.jsonService.getData()
        expectedMostRecentData = {
            "1. open": "358.0200",
            "2. high": "358.0200",
            "3. low": "357.8500",
            "4. close": "357.8800",
            "5. volume": "12932"
        }
        self.assertEqual(actualMostRecentData, expectedMostRecentData)

        # Penultimate
        actualPenultimateData = self.jsonService.getData(-2)
        expectedPenultimateData = {
            "1. open": "357.9200",
            "2. high": "358.0600",
            "3. low": "357.7800",
            "4. close": "357.9450",
            "5. volume": "325931"
        }
        self.assertEqual(actualPenultimateData, expectedPenultimateData)