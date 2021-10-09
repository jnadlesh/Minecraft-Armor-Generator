import json
import random as r

file = open('./data.json')
data = json.load(file)

class Armor: 
    a_adjective = ""
    a_types = ""
    a_bonus = ""
    a_enchantments = ""

#def __str__(self):
    #return "{} {} {} {}".format(self.a_adjectives, self.a_types, self.a_bonus, self.a_enchantments)


def addNumber(x):
    i = ""
    if x == "Mending":
        pass
    elif x == "Unbreaking":
        rnd_number = r.randrange(3)
        if rnd_number == 0:
            i = "I"
        if rnd_number == 1:
            i = "II"
        if rnd_number == 2:
            i = "III"
    else:
        rnd_number = r.randrange(4)
        if rnd_number == 0:
            i = "I"
        if rnd_number == 1:
            i = "II"
        if rnd_number == 2:
            i = "III"
        if rnd_number == 3:
            i = "IV"
    return i


def generateArmor(): 
    
    new_armor = Armor() 

    adjectives = data["adjectives"]
    types = data["types"]
    bonus = "with"
    enchantments = data["enchantment"]
    new_enchantments = ""

    new_armor.a_adjective = adjectives[r.randrange(0, len(adjectives))]
    new_armor.a_types = types[r.randrange(0, len(types))] 

    index = r.randint(0,1) 
    new_list = [] 

    if index == 1: 

        new_armor.a_bonus = bonus
        new_armor.a_enchantments = enchantments[r.randrange(0, len(enchantments))] 
        new_list.append(new_armor.a_enchantments) 
        if new_armor.a_enchantments == "Mending":
            pass
        else:
            new_armor.a_enchantments_number = addNumber(new_armor.a_enchantments)
            new_armor.a_enchantments += " " + new_armor.a_enchantments_number


        index = r.randint(0,1) 
        while index == 1:
            new_enchantments = enchantments[r.randrange(0, len(enchantments))]
            if new_enchantments not in new_list:
                new_list.append(new_enchantments)
                if new_enchantments == "Mending":
                    pass
                else:
                    new_enchantment_number = addNumber(new_enchantments)
                    new_enchantments += " " + new_enchantment_number
                new_armor.a_enchantments += ", " + new_enchantments 

            index = r.randint(0,1)

        else:
            print("{} {} {} {}".format(new_armor.a_adjective, new_armor.a_types, new_armor.a_bonus, new_armor.a_enchantments))
    else:
        print("{} {}".format(new_armor.a_adjective, new_armor.a_types))


def generateList():
    i = 0
    while i < 500:
        generateArmor()
        i += 1

generateList()

