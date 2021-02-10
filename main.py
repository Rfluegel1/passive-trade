import urllib.request
import json

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('AVApiKey.txt', 'r') as apiKey:
        API_KEY = apiKey.readline()

    TIME_SERIES_INTRADAY = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=VOO&interval=5min&apikey=' + API_KEY

    with urllib.request.urlopen(TIME_SERIES_INTRADAY) as response:
        data = json.load(response)

    print(data)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
