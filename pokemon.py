import requests
import json

pokemon = []

r = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1200').json()['results']

for val in r:
    url = val['url']
    u = requests.get(url).json()
    # print(u['sprites']['front_default'])

    data = {
        "name": val["name"],
        "details": val["url"],
        "img": u['sprites']['front_default']
        }

    pokemon.append(data)

# print(pokemon)

with open("pokemon.json", "w") as w:
    json.dump(pokemon, w)
