import csv
import json

parsedini = list()

def readCSV(filename):
    with open(filename, 'rb+') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parsedini.append(row)

def writeJSON(filename):
    with open(filename, 'wb+') as jsonfile:
        json.dump(parsedini, jsonfile)

readCSV('gameusersettings.csv')
writeJSON('gameusersettings.json')