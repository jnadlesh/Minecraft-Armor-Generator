import json
import random as r
import timeit

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
    elif x == "Frost Walker":
        rnd_number = r.randrange(2)
        if rnd_number == 0:
            i = "I"
        if rnd_number == 1:
            i = "II"
    elif x == "Unbreaking" or x == "Thorns" or x == "Soul Speed" or x == "Depth Stider" or x == "Respiration":
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
    enchantment_helmet = data["enchantment_helmet"]
    enchantment_chestplate = data["enchantment_chestplate"]
    enchantment_leggings = data["enchantment_leggings"]
    enchantment_boots = data["enchantment_boots"]
    new_enchantments = ""

    new_armor.a_adjective = adjectives[r.randrange(0, len(adjectives))]
    new_armor.a_types = types[r.randrange(0, len(types))] 

    index = r.randint(0,1) 
    new_list = [] 

    if index == 1: 

        new_armor.a_bonus = bonus
        if new_armor.a_types == "Helmet":
            new_armor.a_enchantments = enchantment_helmet[r.randrange(0, len(enchantment_helmet))]
        if new_armor.a_types == "Chestplate":
            new_armor.a_enchantments = enchantment_chestplate[r.randrange(0, len(enchantment_chestplate))] 
        if new_armor.a_types == "Leggings":
            new_armor.a_enchantments = enchantment_leggings[r.randrange(0, len(enchantment_leggings))] 
        if new_armor.a_types == "Boots":
            new_armor.a_enchantments = enchantment_boots[r.randrange(0, len(enchantment_boots))] 
            if new_armor.a_enchantments == "Frost Walker":
                new_list.append("Depth Strider")
            if new_armor.a_enchantments == "Depth Strider":
                new_list.append("Frost Walker")
        new_list.append(new_armor.a_enchantments) 
        if new_armor.a_enchantments == "Mending":
            pass
        elif new_armor.a_enchantments == "Aqua Affinity":
            pass
        else:
            new_armor.a_enchantments_number = addNumber(new_armor.a_enchantments)
            new_armor.a_enchantments += " " + new_armor.a_enchantments_number


        index = r.randint(0,1) 
        while index == 1:
            if new_armor.a_types == "Helmet":
                new_enchantments = enchantment_helmet[r.randrange(0, len(enchantment_helmet))]
            if new_armor.a_types == "Chestplate":
                new_enchantments = enchantment_chestplate[r.randrange(0, len(enchantment_chestplate))] 
            if new_armor.a_types == "Leggings":
                new_enchantments = enchantment_leggings[r.randrange(0, len(enchantment_leggings))] 
            if new_armor.a_types == "Boots":
                new_enchantments = enchantment_boots[r.randrange(0, len(enchantment_boots))]
                if new_enchantments == "Frost Walker":
                    new_list.append("Depth Strider")
                if new_enchantments == "Depth Strider":
                    new_list.append("Frost Walker")
            if new_enchantments not in new_list:
                new_list.append(new_enchantments)
                if new_enchantments == "Mending":
                    pass
                elif new_enchantments == "Aqua Affinity":
                    pass
                else:
                    new_enchantment_number = addNumber(new_enchantments)
                    new_enchantments += " " + new_enchantment_number
                new_armor.a_enchantments += ", " + new_enchantments 

            index = r.randint(0,1)

        else:
            armor_with_enchants = ("{} {} {} {}".format(new_armor.a_adjective, new_armor.a_types, new_armor.a_bonus, new_armor.a_enchantments))
            return armor_with_enchants
    else:
        armor_without_enchants = ("{} {}".format(new_armor.a_adjective, new_armor.a_types))
        return armor_without_enchants

def generate_list(length):
    """Generate list of armor. No duplicates."""
    seconds = 0
    st = timeit.default_timer()
    f = open("armor.txt", "r+")
    f.truncate()
    f.close()
    armor_list = []
    for i in range(length):
        newArmor = generateArmor()

        dupe = False
        for arm in armor_list:
            if(arm == newArmor):
                dupe = True
                break

        if not dupe:
            armor_list.append(newArmor)
    
    armor_list.sort()
    
    for i in range(len(armor_list)):
        f = open("armor.txt", "a")
        f.write(armor_list[i] + "\n")
        f.close()
    seconds = round(timeit.default_timer() - st)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if seconds > 0 and minutes == 0 and hour == 0:
        print(len(armor_list), f"Prints to armor.txt in {seconds} second(s)") 
    if minutes > 0 and hour == 0:
        print(len(armor_list), f"Prints to armor.txt in {minutes} minute(s) and {seconds} second(s)")
    if hour > 0:
        print(len(armor_list), f"Prints to armor.txt in {hour} hour(s), {minutes} minute(s), and {seconds} second(s)")







generate_list(50000)