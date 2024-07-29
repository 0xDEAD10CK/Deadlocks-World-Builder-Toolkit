import random

lowLevel = [
    "Gain invisibility for 1 minute",
    "Gain one use of Fire Breathing",
    "Gain night vision for 1 minute",
    "Heal 5 HP instantly",
    "Increase movement speed by 10 feet for 1 minute",
    "Gain resistance to fire damage for 1 minute",
    "Gain advantage on your next attack roll",
    "Understand all spoken languages for 1 minute",
    "Gain the ability to breathe underwater for 1 minute",
    "Cure one disease",
    "Remove one level of exhaustion",
    "Gain proficiency in a skill of your choice for 1 minute",
    "Gain 1d4 temporary hit points",
    "Gain the ability to see through walls for 30 seconds",
    "Gain advantage on your next saving throw",
    "Summon a small animal companion for 1 minute",
    "Gain resistance to poison damage for 1 minute",
    "Gain the ability to cast the 'Message' cantrip for 1 minute",
    "Gain +1 to your next ability check",
    "Gain darkvision up to 30 feet for 1 minute",
    "Gain the ability to speak with animals for 1 minute",
    "Gain the ability to climb walls for 1 minute",
    "Gain resistance to cold damage for 1 minute",
    "Gain the ability to detect magic for 1 minute",
    "Gain the ability to walk on water for 1 minute",
    "Gain the ability to jump twice as high for 1 minute",
    "Gain the ability to cast the 'Mage Hand' cantrip for 1 minute",
    "Gain resistance to necrotic damage for 1 minute",
    "Gain the ability to see invisible creatures for 1 minute",
    "Gain +1 to your AC for 1 minute",
    "Gain the ability to understand written languages for 1 minute",
    "Gain the ability to cast the 'Prestidigitation' cantrip for 1 minute"
]

midLevel = [
    "Gain invisibility for 10 minutes",
    "Heal 15 HP instantly",
    "Gain resistance to all damage types for 1 minute",
    "Increase movement speed by 20 feet for 10 minutes",
    "Gain advantage on attack rolls for 1 minute",
    "Gain the ability to fly for 1 minute",
    "Gain the ability to cast the 'Shield' spell once",
    "Gain the ability to speak and understand any language for 10 minutes",
    "Gain the ability to breathe underwater for 10 minutes",
    "Gain immunity to poison for 10 minutes",
    "Gain the ability to cast the 'Invisibility' spell once",
    "Gain proficiency in all saving throws for 10 minutes",
    "Gain resistance to radiant damage for 10 minutes",
    "Gain the ability to cast the 'Detect Thoughts' spell once",
    "Gain 10 temporary hit points",
    "Gain the ability to see through walls for 1 minute",
    "Gain advantage on all skill checks for 10 minutes",
    "Gain the ability to summon a familiar for 10 minutes",
    "Gain the ability to teleport up to 30 feet once",
    "Gain resistance to psychic damage for 10 minutes",
    "Gain the ability to cast the 'Levitate' spell once",
    "Gain the ability to cast the 'Mirror Image' spell once",
    "Gain resistance to thunder damage for 10 minutes",
    "Gain the ability to cast the 'Blur' spell once",
    "Gain the ability to understand the thoughts of others for 10 minutes",
    "Gain +2 to your AC for 10 minutes",
    "Gain the ability to cast the 'Alter Self' spell once",
    "Gain the ability to walk through walls for 10 minutes",
    "Gain the ability to cast the 'Dispel Magic' spell once",
    "Gain the ability to cast the 'Tongues' spell once",
    "Gain the ability to cast the 'Misty Step' spell once"
]

highLevel = [
    "Gain invisibility for 1 hour",
    "Heal 50 HP instantly",
    "Gain immunity to all damage types for 1 minute",
    "Increase movement speed by 40 feet for 1 hour",
    "Gain the ability to fly for 10 minutes",
    "Gain the ability to cast the 'Greater Invisibility' spell once",
    "Gain the ability to speak and understand any language for 1 hour",
    "Gain the ability to breathe underwater for 1 hour",
    "Gain immunity to poison and disease for 1 hour",
    "Gain the ability to cast the 'Teleport' spell once",
    "Gain the ability to cast the 'True Seeing' spell once",
    "Gain proficiency in all skills for 1 hour",
    "Gain resistance to all damage types for 1 hour",
    "Gain the ability to cast the 'Wish' spell once (with DM approval)",
    "Gain 30 temporary hit points",
    "Gain the ability to see through walls for 10 minutes",
    "Gain advantage on all rolls for 1 hour",
    "Gain the ability to summon a celestial being for 1 hour",
    "Gain the ability to teleport up to 120 feet once",
    "Gain immunity to psychic damage for 1 hour",
    "Gain the ability to cast the 'Etherealness' spell once",
    "Gain the ability to cast the 'Polymorph' spell once",
    "Gain resistance to all elemental damage for 1 hour",
    "Gain the ability to cast the 'Shapechange' spell once",
    "Gain the ability to control time for 1 minute (DM discretion)",
    "Gain +5 to your AC for 1 hour",
    "Gain the ability to cast the 'Resurrection' spell once",
    "Gain the ability to walk through walls for 1 hour",
    "Gain the ability to cast the 'Meteor Swarm' spell once",
    "Gain the ability to cast the 'Mind Blank' spell once",
    "Gain the ability to cast the 'Gate' spell once"
]


lowLevelMin = 200
lowLevelMax = 600

midLevelMin = 800
midLevelMax = 1500

highLevelMin = 2000
highLevelMax = 5000


def generate_potion(effect_count):
    effects = []
    price = 0
    for i in range(effect_count):
        roll = random.randint(1, 100)
        
        if 0 < roll < 60:
            effects.append(random.choice(lowLevel) + ".")
            price = price + random.randrange(lowLevelMin, lowLevelMax, 100)
        elif 61 < roll < 85:
            effects.append(random.choice(midLevel) + ".")
            price = price + random.randrange(midLevelMin, midLevelMax, 100)
        else:
            effects.append(random.choice(highLevel) + ".")
            price = price + random.randrange(highLevelMin, highLevelMax, 100)
    
    return {"effects": effects, "price": price}
    
    
print(generate_potion(2))