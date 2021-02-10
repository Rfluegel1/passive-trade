import unittest
import json

from JsonService import JsonService

with open('VOO.json') as VOOJson:
    sample_json = json.load(VOOJson)


class TestJsonService(unittest.TestCase):
    def setUp(self):
        self.jsonService = JsonService


class TestGetters(TestJsonService):
    def testGetLastUpdate(self):
        assert(self.jsonService.getLastUpdate(self) == '')
