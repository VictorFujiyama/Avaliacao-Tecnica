import requests
import time

class StarWarsAPI:

    def __init__(self):
        self.rCharacter = requests.get('https://swapi.dev/api/people')
        self.rWorlds = requests.get('https://swapi.dev/api/planets')
        self.packageCharacterJson = self.rCharacter.json()
        self.packageWorldJson = self.rWorlds.json()
        self.dataCharList = []
        self.dataWorldList = []

    def getPeopleData(self, filterFilms=4):
        print("Request de dados dos personagems em andamento.")
        for package in self.packageCharacterJson['results']:


            if len(package['films']) >= filterFilms:
                rWorlds = requests.get(package['homeworld'])
                worldJson = rWorlds.json()

                dataCharacter = {

                    'name': package['name'],
                    'total films': len(package['films']),
                    'films': package['films'],
                    'homeWorld': worldJson['name']
                }

                self.dataCharList.append(dataCharacter)

                time.sleep(self.rCharacter.elapsed.total_seconds())
        print("Concluido.")
        return self.dataCharList

    def getWorldData(self, filterResidents=5):
        print("Request de dados dos mundos em andamento.")
        for packageW in self.packageWorldJson['results']:

            if len(packageW['residents']) >= filterResidents:
                dataWorlds = {

                    'name': packageW['name'],
                    'population': packageW['population'],
                    'total residents': len(packageW['residents'])
                }
                self.dataWorldList.append(dataWorlds)
                time.sleep(self.rWorlds.elapsed.total_seconds())
        print("Concluido.")

        print("Lista gerada com sucesso!")

        return self.dataWorldList


