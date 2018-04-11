import json


def readJson(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
        return data