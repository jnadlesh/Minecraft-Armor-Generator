'''
My original idea in code
'''


import json
import random as r

file = open('./data.json')
data = json.load(file)

adjective = data["adjectives"]
types = data["types"]
bonus = data["bonus"]
enchantment = data["enchantment"]

def generateArmor():
    index1 = r.randrange(len(adjective))
    index1 = adjective[index1]
    index2 = r.randrange(len(types))
    index2 = types[index2]
    a = r.randint(1,2)
    if (a == 1):
        bonus = data["bonus"]
        bonus = bonus[0]
        index3 = r.randrange(len(enchantment))
        index3 = enchantment[index3]
        print(f"{index1} {index2} {(bonus)} {index3}")
    else:
        print(f"{index1} {index2}")


generateArmor()

