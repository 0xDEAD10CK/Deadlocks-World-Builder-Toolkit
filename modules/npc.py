import random
from .FantasyNames import gen_name

ages = ["young", "middle-aged", "elderly"]
races = ["human", "elf", "dwarf", "orc", "halfling", "gnome"]
hairColors = ["black", "brown", "blonde", "red", "gray", "white"]
hairLengths = ["short", "medium-length", "long", "bald"]
eyeDescriptors = [
    "Gleaming", "Glazed", "Sparkly", "Almond-shaped", "Glistening", "Swollen", "Steady", 
    "Asymmetrical", "Dazzling", "Glittering", "Sunken", "Bug-eyed", "Glowing", "Tear-filled", 
    "Cross-eyed", "Close-set", "Teary", "Deep-set", "Tired", "Doe", "Twinkling", "Downturned", 
    "Guileless", "Vapid", "Elongated", "Watchful", "Watering", "Hooded", "Heavy", "Wide awake", 
    "Huge", "Iridescent", "Heavy-lidded", "Wild-eyed", "Large", "Ablaze", "Lidded", "Icy", 
    "Luminous", "Angelic", "Limpid", "Oval", "Moon-eyed", "Puffy", "Magnificent", "Misty", 
    "Radiant", "Round", "Narrowed", "Slanted", "Golden", "Uneven", "Symmetrical", "Bloodshot", 
    "Angry", "Anxious", "Droopy", "Blue", "Drowsy", "Expressive", "Emotionless", "Keen", 
    "Hollow", "Sad", "Pensive", "Hopeful", "Weary", "Dark", "Pale"
]

eyeColors = ["Black", "Blue", "Blue-green", "Emerald", "Hazel", "Brown", "Clear", "Amber"]

skinColors = [
    "fair", "tan", "dark", "pale", "olive", "ashen", "bronze", "golden", 
    "silver", "copper", "pearly", "iridescent", "emerald green", "sapphire blue", 
    "ruby red", "amethyst purple", "obsidian black", "marble white", "crystal clear", 
    "glowing", "translucent", "mossy green", "lava red", "frosty blue", "dusky", 
    "moonlit", "starry", "galaxy patterned", "misty gray", "shadowy", "celestial", 
    "aquamarine", "fiery orange", "dusky rose", "ghostly pale", "glistening", 
    "stormy gray", "twilight", "dawn-hued", "dusk-hued", "frost-kissed", "sunburnt", 
    "rainbow-hued", "cosmic black", "platinum", "iron", "sandstone", "midnight blue"
]

skinTypes = ["smooth", "rough", "scarred", "freckled"]

jobTitles = [
    "blacksmith", "merchant", "wizard", "warrior", "farmer", "thief", "alchemist", "archer", 
    "bard", "beastmaster", "cleric", "druid", "enchanter", "healer", "knight", "necromancer", 
    "paladin", "ranger", "sorcerer", "spy", "assassin", "shaman", "monk", "witch", "warlock", 
    "bard", "sage", "illusionist", "artificer", "summoner", "hunter", "seamstress", "innkeeper", 
    "guard", "sailor", "pirate", "captain", "sellsword", "mercenary", "trader", "herbalist", 
    "tavern owner", "minstrel", "fortune teller", "oracle", "fletcher", "apothecary", 
    "gemcutter", "jeweler", "cartographer", "beast tamer", "dungeon master", "champion", 
    "hermit", "sage", "seer", "time traveler", "archmage", "spellblade", "shadow dancer", 
    "witch doctor", "elementalist", "geomancer", "wind caller", "firestarter", "ice sculptor", 
    "storm bringer", "moon priestess", "sun warrior", "star navigator", "shadow priest", 
    "dark knight", "light bearer", "crystal mage", "blood mage", "spirit walker", "dream weaver"
]

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