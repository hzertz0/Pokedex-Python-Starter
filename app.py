import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

"""input = input("Search: ").capitalize()

for pokemon in data:
    if input in pokemon["name"]["english"]:
        print(pokemon)"""

"""for pokemon in data:
    if "Grass" in pokemon["type"] and "Poison" in pokemon["type"]:
        print(pokemon["name"]["english"])"""

for pokemon in data:
    if (pokemon["type"][0][:1]) == (pokemon["type"][1][:1]):
        print(pokemon)


