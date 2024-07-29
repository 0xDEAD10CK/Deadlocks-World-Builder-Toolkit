import random
from .FantasyNames import gen_name

ages = ["young", "middle-aged", "elderly"]
races = ["human", "elf", "dwarf", "orc", "halfling", "gnome"]
hairColors = ["black", "brown", "blonde", "red", "gray", "white"]
hairLengths = ["short", "medium-length", "long", "bald"]
eyeDescriptors = ["Gleaming", "Glazed", "Sparkly", "Almond-shaped", "Glistening", "Swollen", "Steady"]
eyeColors = ["Black", "Blue", "Blue-green", "Emerald", "Hazel", "Brown", "Clear", "Amber"]
skinColors = ["fair", "tan", "dark", "pale", "olive", "ashen", "bronze", "golden", "silver", "copper", "pearly"]
skinTypes = ["smooth", "rough", "scarred", "freckled"]
jobTitles = ["blacksmith", "merchant", "wizard", "warrior", "farmer", "thief", "alchemist", "archer", "bard"]

def generateNPC():
    npc = {
        "name": gen_name(),
        "age": random.choice(ages),
        "race": random.choice(races),
        "hairColor": random.choice(hairColors),
        "hairLength": random.choice(hairLengths),
        "eyeDescriptor": random.choice(eyeDescriptors),
        "eyeColor": random.choice(eyeColors),
        "skinColor": random.choice(skinColors),
        "skinType": random.choice(skinTypes),
        "jobTitle": random.choice(jobTitles).capitalize()
    }
    return npc