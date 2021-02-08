import requests
import io
import csv
from bs4 import BeautifulSoup
from urllib.parse import quote


class ArkWikiScraper:
    def __init__(self):
        self.httpSession = requests.Session()
        self.baseUrl = 'https://ark.gamepedia.com/api.php?'
        self.commonParams = [
            'action=parse',
            'format=json',
            'prop=' + quote('text|modules|jsconfigvars'),
        ]
        self.scrapeData = {
            'SpawnEntries': [],
            'ItemIDs': [],
            'BeaconIDs': [],
            'ColorIDs': [],
            'EngramClassNames': [],
            'CreatureIDs': []
        }

    def _getRequest(self, params):
        return self.httpSession.get(
            self.baseUrl +
            '&'.join(self.commonParams) +
            '&'.join(params)
            )

    def scrapeSpawnEntries(self):
        params = [
            'title=Spawn_Entries',
            'text=' + quote('{{:Spawn Entries}}')
        ]
        response = self._getRequest(params)
        data = response.json()['parse']['text']['*']
        soup = BeautifulSoup(data, 'html.parser')

        tables = soup.find_all('table')
        for table in tables:
            if table.caption is not None:
                self.scrapeData['SpawnEntries'].append
                (table.caption.text.rstrip())

        # list(entries)[1].ul.text
        # list(entries)[0].td.text

    def scrapeBeaconIDs(self):
        params = [
            'title=Beacon_IDs',
            'text=' + quote('{{:Beacon IDs}}')
            ]
        response = self._getRequest(params)
        data = response.json()['parse']['text']['*']
        soup = BeautifulSoup(data, 'html.parser')

        tables = soup.find_all('table')
        for table in tables:
            if table.caption is not None:
                self.scrapeData['BeaconIDs'].append(
                    table.caption.text.rstrip())

        # list(entries)[1].ul.text
        # list(entries)[0].td.text

    def scrapeColorIDs(self):
        params = [
            'title=Color_IDs',
            'text=' + quote('{{:Color IDs}}')
            ]
        response = self._getRequest(params)
        data = response.json()['parse']['text']['*']
        soup = BeautifulSoup(data, 'html.parser')

        for row in soup.table.find_all('tr'):
            for col in row.find_all('td'):
                self.scrapeData['ColorIDs'].append(col.text)
        # list(entries)[1].ul.text
        # list(entries)[0].td.text

    def scrapeEngramClassnames(self):
        params = [
            'title=Engram_Classnames',
            'text=' + quote('{{:Engram Classnames}}')
            ]
        response = self._getRequest(params)
        data = response.json()['parse']['text']['*']
        soup = BeautifulSoup(data, 'html.parser')

        for row in soup.table.find_all('tr'):
            for col in row.find_all('td'):
                self.scrapeData['EngramClassnames'].append(col.text)
        # list(entries)[1].ul.text
        # list(entries)[0].td.text

    def scrapeCreatureIDs(self):
        params = [
            'title=Creature_IDs',
            'text=' + quote('{{:Creature IDs}}')
            ]
        response = self._getRequest(params)
        data = response.json()['parse']['text']['*']
        soup = BeautifulSoup(data, 'html.parser')

        for table in soup.find_all('table'):
            self.scrapeData['CreatureIDs'].append(table.th)
        # list(entries)[1].ul.text
        # list(entries)[0].td.text

    def scrapeItemIDs(self):
        categories = [
            'Resources',
            'Tools',
            'Armor',
            'Saddles',
            'Structures',
            'Dye',
            'Consumables',
            'Recipes',
            'Eggs',
            'Farming',
            'Seeds',
            'Weapons and Attachments',
            'Ammunition',
            'Skins',
            'Artifacts',
            'Trophies'
            ]
        header = [
            'Title',
            'Image',
            'Category',
            'Stack',
            'ItemID',
            'Class',
            'Blueprint'
            ]

        self.scrapeData['ItemIDs'].append(header)
        for cat in categories:  # Candidate for async
            params = [
                'title=' + cat + '_IDs',
                'text=' + quote('{{:Item IDs/' + cat + '}}')
                ]
            response = self._getRequest(params)
            data = response.json()['parse']['text']['*']
            soup = BeautifulSoup(data, 'html.parser')

            for row in soup.find_all('tr'):
                r = row.find_all('td')
                if len(r) > 0:
                    entry = []
                    entry.append(r[0].find('a')['title'])  # Item Title
                    entry.append(r[0].find('a').find('img')['src'])  # Item Icon Link
                    entry.append(r[1].find('a').text)  # Category
                    entry.append(r[2].text)  # Stack Size
                    entry.append(r[3].text.lstrip())  # Item ID
                    entry.append(r[4].text.rstrip())  # Item Spawn Class
                    entry.append(r[5].text.rstrip())  # Blueprint Path
                    self.scrapeData['ItemIDs'].append(entry)

    def toCSV(self):
        f = io.StringIO()
        writer = csv.writer(f)
        for item in self.scrapeData['ItemIDs']:
            writer.writerow(item)
        return f


def main():
    pass


if __name__ == '__main__':
    main()
