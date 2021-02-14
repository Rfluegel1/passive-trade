
class JsonService:

    def __init__(self, json=''):
        self.json = json

    def getMostRecentData(self, header='Time Series (5min)'):
        key = list(self.json[header])[-1]
        data = self.json[header][key]
        return data

    def getPenultimateData(self, header='Time Series (5min)'):
        key = list(self.json[header])[-2]
        data = self.json[header][key]
        return data
