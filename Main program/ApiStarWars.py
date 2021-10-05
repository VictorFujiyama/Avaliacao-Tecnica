from Request import *
import json


def main():
    result = []
    api = StarWarsAPI()
    peoplelist = api.getPeopleData()
    worldlist = api.getWorldData()

    filmsdata = {
        'People with 4 or more films:': len(peoplelist),
        'Character infos:': peoplelist[:],
        'Worlds with 5 or more residents:': len(worldlist),
        'Worlds infos:': worldlist[:]
    }

    result.append(filmsdata)
    with open('StarWarsAPI.json', 'w') as f:
        json.dump(result, f, indent=2)


if __name__ == '__main__':
    main()
