
class JsonService:

    def __init__(self, json=''):
        self.json = json

    def getData(self, index=-1, header='Time Series (5min)'):
        key = list(self.json[header])[index]
        data = self.json[header][key]
        return data
