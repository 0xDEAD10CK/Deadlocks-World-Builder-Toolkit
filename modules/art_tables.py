import random

def roll_25_gp_art_object():
    """Returns a 25 GP art object based on a d10 roll."""
    art_objects_25_gp = [
        "25gp: Silver ewer",
        "25gp: Carved bone statuette",
        "25gp: Small gold bracelet",
        "25gp: Cloth-of-gold vestments",
        "25gp: Black velvet mask stitched with silver thread",
        "25gp: Copper chalice with silver filigree",
        "25gp: Pair of engraved bone dice",
        "25gp: Small mirror set in a painted wooden frame",
        "25gp: Embroidered silk handkerchief",
        "25gp: Gold locket with a painted portrait inside"
    ]
    roll = random.randint(1, 10) - 1  # Roll a d10 (1-10) and adjust for 0-indexed list
    return art_objects_25_gp[roll]
	
def roll_250_gp_art_object():
    """Returns a 250 GP art object based on a d10 roll."""
    art_objects_250_gp = [
        "250gp: Gold ring set with bloodstones",
        "250gp: Carved ivory statuette",
        "250gp: Large gold bracelet",
        "250gp: Silver necklace with a gemstone pendant",
        "250gp: Bronze crown",
        "250gp: Silk robe with gold embroidery",
        "250gp: Large well-made tapestry",
        "250gp: Brass mug with jade inlay",
        "250gp: Box of turquoise animal figurines",
        "250gp: Gold bird cage with electrum filigree"
    ]
    roll = random.randint(1, 10) - 1  # Roll a d10 (1-10) and adjust for 0-indexed list
    return art_objects_250_gp[roll]
	
def roll_750_gp_art_object():
    """Returns a 750 GP art object based on a d10 roll."""
    art_objects_750_gp = [
        "750gp: Silver chalice set with moonstones",
        "750gp: Silver-plated steel longsword with jet set in hilt",
        "750gp: Carved harp of exotic wood with ivory inlay and zircon gems",
        "750gp: Small gold idol",
        "750gp: Gold dragon comb set with red garnets as eyes",
        "750gp: Bottle stopper cork embossed with gold leaf and set with amethysts",
        "750gp: Ceremonial electrum dagger with a black pearl in the pommel",
        "750gp: Silver and gold brooch",
        "750gp: Obsidian statuette with gold fittings and inlay",
        "750gp: Painted gold war mask"
    ]
    roll = random.randint(1, 10) - 1  # Roll a d10 (1-10) and adjust for 0-indexed list
    return art_objects_750_gp[roll]
	
def roll_2500_gp_art_object():
    """Returns a 2500 GP art object based on a d10 roll."""
    art_objects_2500_gp = [
        "2500gp: Fine gold chain set with a fire opal",
        "2500gp: Old masterpiece painting",
        "2500gp: Embroidered silk and velvet mantle set with numerous moonstones",
        "2500gp: Platinum bracelet set with a sapphire",
        "2500gp: Embroidered glove set with jewel chips",
        "2500gp: Jeweled anklet",
        "2500gp: Gold music box",
        "2500gp: Gold circlet set with four aquamarines",
        "2500gp: Eye patch with a mock eye set in blue sapphire and moonstone",
        "2500gp: A necklace string of small pink pearls"
    ]
    roll = random.randint(1, 10) - 1  # Roll a d10 (1-10) and adjust for 0-indexed list
    return art_objects_2500_gp[roll]
	
def roll_7500_gp_art_object():
    """Returns a 7500 GP art object based on a d10 roll."""
    art_objects_7500_gp = [
        "7500gp: Jeweled gold crown",
        "7500gp: Jeweled platinum ring",
        "7500gp: Small gold statuette set with rubies",
        "7500gp: Gold cup set with emeralds",
        "7500gp: Gold jewelry box with platinum filigree",
        "7500gp: Painted gold child's sarcophagus",
        "7500gp: Jade game board with solid gold playing pieces",
        "7500gp: Bejeweled ivory drinking horn with gold filigree"
    ]
    roll = random.randint(1, 10) - 1  # Roll a d10 (1-10) and adjust for 0-indexed list
    return art_objects_7500_gp[roll]