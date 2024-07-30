import random
from .FantasyNames import gen_name

def generate_name():
    names = ["The Silver Stag", "The Golden Goose", "The Drunken Dragon", "The Whispering Willow"]
    return random.choice(names)

def generate_location():
    locations = [
        "in the heart of the bustling city of Alden",
        "nestled at the edge of the Whispering Woods",
        "along the banks of the River Serene",
        "at the crossroads of the old trade routes"
    ]
    return random.choice(locations)

def generate_appearance():
    appearances = [
        "a large, cozy building with wooden beams and a thatched roof",
        "a grand stone structure with ivy-covered walls",
        "a small, run-down building with a creaky sign",
        "a quaint, charming inn with colorful flowers in the windows"
    ]
    return random.choice(appearances)

def generate_owner():
    owners = [
        {"name": gen_name(), "description": "a former adventurer with a kind heart and a sharp wit"},
        {"name": gen_name(), "description": "a retired dwarf warrior with many tales of battle"},
        {"name": gen_name(), "description": "a mysterious elf with a deep knowledge of herbalism"},
        {"name": gen_name(), "description": "a charismatic bard with a love for stories and songs"}
    ]
    return random.choice(owners)

def generate_menu():
    foods = ["Rabbit stew", "Freshly baked bread", "Forest Delight", "Grilled fish"]
    drinks = ["Whispering Ale", "Elven mead", "Berry juice", "Dwarven stout"]
    return {
        "food": random.sample(foods, 3),
        "drinks": random.sample(drinks, 3)
    }

def generate_patrons():
    regulars = [
        {"name": "Old Tom", "description": "a retired sailor with tales of the sea"},
        {"name": "Mira", "description": "a local herbalist often seen with her pet cat"},
        {"name": "Borik", "description": "a grumpy dwarf miner"},
        {"name": "Sylvia", "description": "a traveling bard with a beautiful voice"}
    ]
    travelers = [
        {"description": "a group of dwarven miners on their way to the mountains"},
        {"description": "a lone elf studying an ancient map"},
        {"description": "a pair of human merchants trading goods"},
        {"description": "a mysterious cloaked figure in the corner"}
    ]
    notable_figures = [
        {"name": "Sir Galen", "description": "a knight of the realm, known for his bravery and loyalty"},
        {"name": "Lady Arwen", "description": "a noblewoman with a secretive past"},
        {"name": "Thorn", "description": "a renowned thief with a bounty on his head"},
        {"name": "Eldrin", "description": "a powerful mage in search of ancient knowledge"}
    ]
    return {
        "regulars": random.sample(regulars, 2),
        "travelers": random.sample(travelers, 2),
        "notable_figures": random.sample(notable_figures, 1)
    }

def generate_staff():
    bartenders = [
        {"name": "Jorin", "description": "a jovial man with a knack for storytelling"},
        {"name": "Kara", "description": "a no-nonsense woman with a soft spot for regulars"},
        {"name": "Darin", "description": "a young man eager to prove himself"},
        {"name": "Lyria", "description": "a former adventurer with many tales"}
    ]
    cooks = [
        {"name": "Bessa", "description": "a stern woman with a reputation for her amazing pies"},
        {"name": "Gorim", "description": "a gruff dwarf with a talent for hearty meals"},
        {"name": "Sela", "description": "an elf with a passion for exotic dishes"},
        {"name": "Tomas", "description": "a cheerful man who loves to experiment with new recipes"}
    ]
    return {
        "bartender": random.choice(bartenders),
        "cook": random.choice(cooks)
    }

def generate_atmosphere():
    music = [
        "a bard playing a soft tune on his lute",
        "a lively band of minstrels",
        "a solitary flute player in the corner",
        "the gentle hum of patrons chatting"
    ]
    lighting = [
        "warm, flickering candlelight casting cozy shadows",
        "bright magical lanterns",
        "dim, with a few strategically placed candles",
        "soft, enchanting glow from enchanted crystals"
    ]
    smells = [
        "the rich aroma of roasting meat and fresh herbs",
        "the scent of freshly baked bread",
        "a hint of lavender and other herbs",
        "the smell of spilled ale and wood smoke"
    ]
    return {
        "music": random.choice(music),
        "lighting": random.choice(lighting),
        "smells": random.choice(smells)
    }

def generate_plot_hooks():
    quests = [
        {"description": "a notice seeking brave souls to investigate strange lights in the Whispering Woods"},
        {"description": "a job posting for a guard to protect a merchant caravan"},
        {"description": "a request to find a missing person last seen in the area"},
        {"description": "a call for help to solve a series of thefts in the village"}
    ]
    rumors = [
        {"description": "whisperings of a hidden treasure buried beneath the inn"},
        {"description": "rumors of a ghost haunting the nearby forest"},
        {"description": "talk of a secret cult operating in the area"},
        {"description": "news of a rare magical artifact recently discovered"}
    ]
    requests = [
        {"description": "the owner asks the players to help find her missing brother"},
        {"description": "a local farmer seeks assistance with a monster terrorizing his livestock"},
        {"description": "a traveling merchant needs guards for his journey"},
        {"description": "a scholar requests help in finding a lost manuscript"}
    ]
    return {
        "quests": random.sample(quests, 1),
        "rumors": random.sample(rumors, 1),
        "requests": random.sample(requests, 1)
    }

def generate_events():
    special_occasions = [
        {"description": "a local festival celebrating the harvest"},
        {"description": "a bard competition drawing talents from far and wide"},
        {"description": "a knightly tournament held in honor of a local lord"},
        {"description": "a mysterious masked ball"}
    ]
    games = [
        {"description": "an arm wrestling contest with a prize for the winner"},
        {"description": "a high-stakes card game drawing a rough crowd"},
        {"description": "a friendly dice game played by the regulars"},
        {"description": "a drinking contest that never ends well"}
    ]
    incidents = [
        {"description": "a mysterious cloaked figure causing a commotion at the bar"},
        {"description": "a bar fight breaking out between two rival groups"},
        {"description": "a sudden appearance of a wild animal inside the tavern"},
        {"description": "a theft that needs immediate attention"}
    ]
    return {
        "special_occasions": random.sample(special_occasions, 1),
        "games": random.sample(games, 1),
        "incidents": random.sample(incidents, 1)
    }

def generate_tavern():
    return {
        "name": generate_name(),
        "location": generate_location(),
        "appearance": generate_appearance(),
        "owner": generate_owner(),
        "menu": generate_menu(),
        "patrons": generate_patrons(),
        "staff": generate_staff(),
        "atmosphere": generate_atmosphere(),
        "plot_hooks": generate_plot_hooks(),
        "events": generate_events()
    }

