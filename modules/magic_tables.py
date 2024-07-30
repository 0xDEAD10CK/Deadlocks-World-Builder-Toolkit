import random

def roll_magic_item_table_a():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 50:
        return "Potion of healing"
    elif 51 <= d100_roll <= 60:
        return "Spell scroll (cantrip)"
    elif 61 <= d100_roll <= 70:
        return "Potion of climbing"
    elif 71 <= d100_roll <= 90:
        return "Spell scroll (1st level)"
    elif 91 <= d100_roll <= 94:
        return "Spell scroll (2nd level)"
    elif 95 <= d100_roll <= 98:
        return "Potion of greater healing"
    elif d100_roll == 99:
        return "Bag of holding"
    elif d100_roll == 100:
        return "Driftglobe"

def roll_magic_item_table_b():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 15:
        return "Potion of greater healing"
    elif 16 <= d100_roll <= 22:
        return "Potion of fire breath"
    elif 23 <= d100_roll <= 29:
        return "Potion of resistance"
    elif 30 <= d100_roll <= 34:
        return "Ammunition, +1"
    elif 35 <= d100_roll <= 39:
        return "Potion of animal friendship"
    elif 40 <= d100_roll <= 44:
        return "Potion of hill giant strength"
    elif 45 <= d100_roll <= 49:
        return "Potion of growth"
    elif 50 <= d100_roll <= 54:
        return "Potion of water breathing"
    elif 55 <= d100_roll <= 59:
        return "Spell scroll (2nd level)"
    elif 60 <= d100_roll <= 64:
        return "Spell scroll (3rd level)"
    elif 65 <= d100_roll <= 67:
        return "Bag of holding"
    elif 68 <= d100_roll <= 70:
        return "Keoghtom's ointment"
    elif 71 <= d100_roll <= 73:
        return "Oil of slipperiness"
    elif 74 <= d100_roll <= 75:
        return "Dust of disappearance"
    elif 76 <= d100_roll <= 77:
        return "Dust of dryness"
    elif 78 <= d100_roll <= 79:
        return "Dust of sneezing and choking"
    elif 80 <= d100_roll <= 81:
        return "Elemental gem"
    elif 82 <= d100_roll <= 83:
        return "Philter of love"
    elif d100_roll == 84:
        return "Alchemy jug"
    elif d100_roll == 85:
        return "Cap of water breathing"
    elif d100_roll == 86:
        return "Cloak of the manta ray"
    elif d100_roll == 87:
        return "Driftglobe"
    elif d100_roll == 88:
        return "Goggles of night"
    elif d100_roll == 89:
        return "Helm of comprehending languages"
    elif d100_roll == 90:
        return "Immovable rod"
    elif d100_roll == 91:
        return "Lantern of revealing"
    elif d100_roll == 92:
        return "Mariner's armor"
    elif d100_roll == 93:
        return "Mithral armor"
    elif d100_roll == 94:
        return "Potion of poison"
    elif d100_roll == 95:
        return "Ring of swimming"
    elif d100_roll == 96:
        return "Robe of useful items"
    elif d100_roll == 97:
        return "Rope of climbing"
    elif d100_roll == 98:
        return "Saddle of the cavalier"
    elif d100_roll == 99:
        return "Wand of magic detection"
    elif d100_roll == 100:
        return "Wand of secrets"
        
def roll_magic_item_table_c():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 15:
        return "Potion of superior healing"
    elif 16 <= d100_roll <= 22:
        return "Spell scroll (4th level)"
    elif 23 <= d100_roll <= 27:
        return "Ammunition, +2"
    elif 28 <= d100_roll <= 32:
        return "Potion of clairvoyance"
    elif 33 <= d100_roll <= 37:
        return "Potion of diminution"
    elif 38 <= d100_roll <= 42:
        return "Potion of gaseous form"
    elif 43 <= d100_roll <= 47:
        return "Potion of frost giant strength"
    elif 48 <= d100_roll <= 52:
        return "Potion of stone giant strength"
    elif 53 <= d100_roll <= 57:
        return "Potion of heroism"
    elif 58 <= d100_roll <= 62:
        return "Potion of invulnerability"
    elif 63 <= d100_roll <= 67:
        return "Potion of mind reading"
    elif 68 <= d100_roll <= 72:
        return "Spell scroll (5th level)"
    elif 73 <= d100_roll <= 75:
        return "Elixir of health"
    elif 76 <= d100_roll <= 78:
        return "Oil of etherealness"
    elif 79 <= d100_roll <= 81:
        return "Potion of fire giant strength"
    elif 82 <= d100_roll <= 84:
        return "Quaal's feather token"
    elif 85 <= d100_roll <= 87:
        return "Scroll of protection"
    elif 88 <= d100_roll <= 89:
        return "Bag of beans"
    elif 90 <= d100_roll <= 91:
        return "Bead of force"
    elif d100_roll == 92:
        return "Chime of opening"
    elif d100_roll == 93:
        return "Decanter of endless water"
    elif d100_roll == 94:
        return "Eyes of minute seeing"
    elif d100_roll == 95:
        return "Folding boat"
    elif d100_roll == 96:
        return "Heward's handy haversack"
    elif d100_roll == 97:
        return "Horseshoes of speed"
    elif d100_roll == 98:
        return "Necklace of fireballs"
    elif d100_roll == 99:
        return "Periapt of health"
    elif d100_roll == 100:
        return "Sending Stones"
        
def roll_magic_item_table_d():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 20:
        return "Potion of supreme healing"
    elif 21 <= d100_roll <= 30:
        return "Potion of invisibility"
    elif 31 <= d100_roll <= 40:
        return "Potion of speed"
    elif 41 <= d100_roll <= 50:
        return "Spell scroll (6th level)"
    elif 51 <= d100_roll <= 57:
        return "Spell scroll (7th level)"
    elif 58 <= d100_roll <= 62:
        return "Ammunition, +3"
    elif 63 <= d100_roll <= 67:
        return "Oil of sharpness"
    elif 68 <= d100_roll <= 72:
        return "Potion of flying"
    elif 73 <= d100_roll <= 77:
        return "Potion of cloud giant strength"
    elif 78 <= d100_roll <= 82:
        return "Potion of longevity"
    elif 83 <= d100_roll <= 87:
        return "Potion of vitality"
    elif 88 <= d100_roll <= 92:
        return "Spell scroll (8th level)"
    elif 93 <= d100_roll <= 95:
        return "Horseshoes of a zephyr"
    elif 96 <= d100_roll <= 98:
        return "Nolzur's marvelous pigments"
    elif d100_roll == 99:
        return "Bag of devouring"
    elif d100_roll == 100:
        return "Portable hole"
        
def roll_magic_item_table_e():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 30:
        return "Spell scroll (8th level)"
    elif 31 <= d100_roll <= 55:
        return "Potion of storm giant strength"
    elif 56 <= d100_roll <= 70:
        return "Potion of supreme healing"
    elif 71 <= d100_roll <= 85:
        return "Spell scroll (9th level)"
    elif 86 <= d100_roll <= 93:
        return "Universal solvent"
    elif 94 <= d100_roll <= 98:
        return "Arrow of slaying"
    elif 99 <= d100_roll <= 100:
        return "Sovereign glue"
        
def roll_magic_item_table_f():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 15:
        return "Weapon, +1"
    elif 16 <= d100_roll <= 18:
        return "Shield, +1"
    elif 19 <= d100_roll <= 21:
        return "Sentinel shield"
    elif 22 <= d100_roll <= 23:
        return "Amulet of proof against detection and location"
    elif 24 <= d100_roll <= 25:
        return "Boots of elvenkind"
    elif 26 <= d100_roll <= 27:
        return "Boots of striding and springing"
    elif 28 <= d100_roll <= 29:
        return "Bracers of archery"
    elif 30 <= d100_roll <= 31:
        return "Brooch of shielding"
    elif 32 <= d100_roll <= 33:
        return "Broom of flying"
    elif 34 <= d100_roll <= 35:
        return "Cloak of elvenkind"
    elif 36 <= d100_roll <= 37:
        return "Cloak of protection"
    elif 38 <= d100_roll <= 39:
        return "Gauntlets of ogre power"
    elif 40 <= d100_roll <= 41:
        return "Hat of disguise"
    elif 42 <= d100_roll <= 43:
        return "Javelin of lightning"
    elif 44 <= d100_roll <= 45:
        return "Pearl of power"
    elif 46 <= d100_roll <= 47:
        return "Rod of the pact keeper, +1"
    elif 48 <= d100_roll <= 49:
        return "Slippers of spider climbing"
    elif 50 <= d100_roll <= 51:
        return "Staff of the adder"
    elif 52 <= d100_roll <= 53:
        return "Staff of the python"
    elif 54 <= d100_roll <= 55:
        return "Sword of vengeance"
    elif 56 <= d100_roll <= 57:
        return "Trident of fish command"
    elif 58 <= d100_roll <= 59:
        return "Wand of magic missiles"
    elif 60 <= d100_roll <= 61:
        return "Wand of the war mage, +1"
    elif 62 <= d100_roll <= 63:
        return "Wand of web"
    elif 64 <= d100_roll <= 65:
        return "Weapon of warning"
    elif d100_roll == 66:
        return "Adamantine armor (chain mail)"
    elif d100_roll == 67:
        return "Adamantine armor (chain shirt)"
    elif d100_roll == 68:
        return "Adamantine armor (scale mail)"
    elif d100_roll == 69:
        return "Bag of tricks (gray)"
    elif d100_roll == 70:
        return "Bag of tricks (rust)"
    elif d100_roll == 71:
        return "Bag of tricks (tan)"
    elif d100_roll == 72:
        return "Boots of the winterlands"
    elif d100_roll == 73:
        return "Circlet of blasting"
    elif d100_roll == 74:
        return "Deck of illusions"
    elif d100_roll == 75:
        return "Eversmoking bottle"
    elif d100_roll == 76:
        return "Eyes of charming"
    elif d100_roll == 77:
        return "Eyes of the eagle"
    elif d100_roll == 78:
        return "Figurine of wondrous power (silver raven)"
    elif d100_roll == 79:
        return "Gem of brightness"
    elif d100_roll == 80:
        return "Gloves of missile snaring"
    elif d100_roll == 81:
        return "Gloves of swimming and climbing"
    elif d100_roll == 82:
        return "Gloves of thievery"
    elif d100_roll == 83:
        return "Headband of intellect"
    elif d100_roll == 84:
        return "Helm of telepathy"
    elif d100_roll == 85:
        return "Instrument of the bards (Doss lute)"
    elif d100_roll == 86:
        return "Instrument of the bards (Fochlucan bandore)"
    elif d100_roll == 87:
        return "Instrument of the bards (Mac-Fuimidh cittern)"
    elif d100_roll == 88:
        return "Medallion of thoughts"
    elif d100_roll == 89:
        return "Necklace of adaptation"
    elif d100_roll == 90:
        return "Periapt of wound closure"
    elif d100_roll == 91:
        return "Pipes of haunting"
    elif d100_roll == 92:
        return "Pipes of the sewers"
    elif d100_roll == 93:
        return "Ring of jumping"
    elif d100_roll == 94:
        return "Ring of mind shielding"
    elif d100_roll == 95:
        return "Ring of warmth"
    elif d100_roll == 96:
        return "Ring of water walking"
    elif d100_roll == 97:
        return "Quiver of Ehlonna"
    elif d100_roll == 98:
        return "Stone of good luck"
    elif d100_roll == 99:
        return "Wind fan"
    elif d100_roll == 100:
        return "Winged boots"
        
def roll_magic_item_table_g():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 11:
        return "Weapon, +2"
    elif 12 <= d100_roll <= 14:
        # Roll a d8 for figurine of wondrous power
        figurine_roll = random.randint(1, 8)
        figurines = {
            1: "Bronze griffon",
            2: "Ebony fly",
            3: "Golden lions",
            4: "Ivory goats",
            5: "Marble elephant",
            6: "Onyx dog",
            7: "Onyx dog",
            8: "Serpentine owl"
        }
        return f"Figurine of wondrous power: {figurines[figurine_roll]}"
    elif d100_roll == 15:
        return "Adamantine armor (breastplate)"
    elif d100_roll == 16:
        return "Adamantine armor (splint)"
    elif d100_roll == 17:
        return "Amulet of health"
    elif d100_roll == 18:
        return "Armor of vulnerability"
    elif d100_roll == 19:
        return "Arrow-catching shield"
    elif d100_roll == 20:
        return "Belt of dwarvenkind"
    elif d100_roll == 21:
        return "Belt of hill giant strength"
    elif d100_roll == 22:
        return "Berserker axe"
    elif d100_roll == 23:
        return "Boots of levitation"
    elif d100_roll == 24:
        return "Boots of speed"
    elif d100_roll == 25:
        return "Bowl of commanding water elementals"
    elif d100_roll == 26:
        return "Bracers of defense"
    elif d100_roll == 27:
        return "Brazier of commanding fire elementals"
    elif d100_roll == 28:
        return "Cape of the mountebank"
    elif d100_roll == 29:
        return "Censer of controlling air elementals"
    elif d100_roll == 30:
        return "Armor, +1 chain mail"
    elif d100_roll == 31:
        return "Armor of resistance (chain mail)"
    elif d100_roll == 32:
        return "Armor of resistance (chain shirt)"
    elif d100_roll == 33:
        return "Armor, +1 chain shirt"
    elif d100_roll == 34:
        return "Cloak of displacement"
    elif d100_roll == 35:
        return "Cloak of the bat"
    elif d100_roll == 36:
        return "Cube of force"
    elif d100_roll == 37:
        return "Daern's instant fortress"
    elif d100_roll == 38:
        return "Dagger of venom"
    elif d100_roll == 39:
        return "Dimensional shackles"
    elif d100_roll == 40:
        return "Dragon slayer"
    elif d100_roll == 41:
        return "Elven chain"
    elif d100_roll == 42:
        return "Flame tongue"
    elif d100_roll == 43:
        return "Gem of seeing"
    elif d100_roll == 44:
        return "Giant slayer"
    elif d100_roll == 45:
        return "Glamoured studded leather"
    elif d100_roll == 46:
        return "Helm of teleportation"
    elif d100_roll == 47:
        return "Horn of blasting"
    elif d100_roll == 48:
        return "Horn of Valhalla (silver or brass)"
    elif d100_roll == 49:
        return "Instrument of the bards (Canaith mandolin)"
    elif d100_roll == 50:
        return "Instrument of the bards (Cii lyre)"
    elif d100_roll == 51:
        return "Ioun stone (awareness)"
    elif d100_roll == 52:
        return "Ioun stone (protection)"
    elif d100_roll == 53:
        return "Ioun stone (reserve)"
    elif d100_roll == 54:
        return "Ioun stone (sustenance)"
    elif d100_roll == 55:
        return "Iron bands of Bilarro"
    elif d100_roll == 56:
        return "Armor, +1 leather"
    elif d100_roll == 57:
        return "Armor of resistance (leather)"
    elif d100_roll == 58:
        return "Mace of disruption"
    elif d100_roll == 59:
        return "Mace of smiting"
    elif d100_roll == 60:
        return "Mace of terror"
    elif d100_roll == 61:
        return "Mantle of spell resistance"
    elif d100_roll == 62:
        return "Necklace of prayer beads"
    elif d100_roll == 63:
        return "Periapt of proof against poison"
    elif d100_roll == 64:
        return "Ring of animal influence"
    elif d100_roll == 65:
        return "Ring of evasion"
    elif d100_roll == 66:
        return "Ring of feather falling"
    elif d100_roll == 67:
        return "Ring of free action"
    elif d100_roll == 68:
        return "Ring of protection"
    elif d100_roll == 69:
        return "Ring of resistance"
    elif d100_roll == 70:
        return "Ring of spell storing"
    elif d100_roll == 71:
        return "Ring of the ram"
    elif d100_roll == 72:
        return "Ring of X-ray vision"
    elif d100_roll == 73:
        return "Robe of eyes"
    elif d100_roll == 74:
        return "Rod of rulership"
    elif d100_roll == 75:
        return "Rod of the pact keeper, +2"
    elif d100_roll == 76:
        return "Rope of entanglement"
    elif d100_roll == 77:
        return "Armor, +1 scale mail"
    elif d100_roll == 78:
        return "Armor of resistance (scale mail)"
    elif d100_roll == 79:
        return "Shield, +2"
    elif d100_roll == 80:
        return "Shield of missile attraction"
    elif d100_roll == 81:
        return "Staff of charming"
    elif d100_roll == 82:
        return "Staff of healing"
    elif d100_roll == 83:
        return "Staff of swarming insects"
    elif d100_roll == 84:
        return "Staff of the woodlands"
    elif d100_roll == 85:
        return "Staff of withering"
    elif d100_roll == 86:
        return "Stone of controlling earth elementals"
    elif d100_roll == 87:
        return "Sun blade"
    elif d100_roll == 88:
        return "Sword of life stealing"
    elif d100_roll == 89:
        return "Sword of wounding"
    elif d100_roll == 90:
        return "Tentacle rod"
    elif d100_roll == 91:
        return "Vicious weapon"
    elif d100_roll == 92:
        return "Wand of binding"
    elif d100_roll == 93:
        return "Wand of enemy detection"
    elif d100_roll == 94:
        return "Wand of fear"
    elif d100_roll == 95:
        return "Wand of fireballs"
    elif d100_roll == 96:
        return "Wand of lightning bolts"
    elif d100_roll == 97:
        return "Wand of paralysis"
    elif d100_roll == 98:
        return "Wand of the war mage, +2"
    elif d100_roll == 99:
        return "Wand of wonder"
    elif d100_roll == 100:
        return "Wings of flying"
        
def roll_magic_item_table_h():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 10:
        return "Weapon, +3"
    elif 11 <= d100_roll <= 12:
        return "Amulet of the planes"
    elif 13 <= d100_roll <= 14:
        return "Carpet of flying"
    elif 15 <= d100_roll <= 16:
        return "Crystal ball (very rare version)"
    elif 17 <= d100_roll <= 18:
        return "Ring of regeneration"
    elif 19 <= d100_roll <= 20:
        return "Ring of shooting stars"
    elif 21 <= d100_roll <= 22:
        return "Ring of telekinesis"
    elif 23 <= d100_roll <= 24:
        return "Robe of scintillating colors"
    elif 25 <= d100_roll <= 26:
        return "Robe of stars"
    elif 27 <= d100_roll <= 28:
        return "Rod of absorption"
    elif 29 <= d100_roll <= 30:
        return "Rod of alertness"
    elif 31 <= d100_roll <= 32:
        return "Rod of security"
    elif 33 <= d100_roll <= 34:
        return "Rod of the pact keeper, +3"
    elif 35 <= d100_roll <= 36:
        return "Scimitar of speed"
    elif 37 <= d100_roll <= 38:
        return "Shield, +3"
    elif 39 <= d100_roll <= 40:
        return "Staff of fire"
    elif 41 <= d100_roll <= 42:
        return "Staff of frost"
    elif 43 <= d100_roll <= 44:
        return "Staff of power"
    elif 45 <= d100_roll <= 46:
        return "Staff of striking"
    elif 47 <= d100_roll <= 48:
        return "Staff of thunder and lightning"
    elif 49 <= d100_roll <= 50:
        return "Sword of sharpness"
    elif 51 <= d100_roll <= 52:
        return "Wand of polymorph"
    elif 53 <= d100_roll <= 54:
        return "Wand of the war mage, +3"
    elif d100_roll == 55:
        return "Adamantine armor (half plate)"
    elif d100_roll == 56:
        return "Adamantine armor (plate)"
    elif d100_roll == 57:
        return "Animated shield"
    elif d100_roll == 58:
        return "Belt of fire giant strength"
    elif d100_roll == 59:
        return "Belt of frost (or stone) giant strength"
    elif d100_roll == 60:
        return "Armor, +1 breastplate"
    elif d100_roll == 61:
        return "Armor of resistance (breastplate)"
    elif d100_roll == 62:
        return "Candle of invocation"
    elif d100_roll == 63:
        return "Armor, +2 chain mail"
    elif d100_roll == 64:
        return "Armor, +2 chain shirt"
    elif d100_roll == 65:
        return "Cloak of arachnida"
    elif d100_roll == 66:
        return "Dancing sword"
    elif d100_roll == 67:
        return "Demon armor"
    elif d100_roll == 68:
        return "Dragon scale mail"
    elif d100_roll == 69:
        return "Dwarven plate"
    elif d100_roll == 70:
        return "Dwarven thrower"
    elif d100_roll == 71:
        return "Efreeti bottle"
    elif d100_roll == 72:
        return "Figurine of wondrous power (obsidian steed)"
    elif d100_roll == 73:
        return "Frost brand"
    elif d100_roll == 74:
        return "Helm of brilliance"
    elif d100_roll == 75:
        return "Horn of Valhalla (bronze)"
    elif d100_roll == 76:
        return "Instrument of the bards (Anstruth harp)"
    elif d100_roll == 77:
        return "Ioun stone (absorption)"
    elif d100_roll == 78:
        return "Ioun stone (agility)"
    elif d100_roll == 79:
        return "Ioun stone (fortitude)"
    elif d100_roll == 80:
        return "Ioun stone (insight)"
    elif d100_roll == 81:
        return "Ioun stone (intellect)"
    elif d100_roll == 82:
        return "Ioun stone (leadership)"
    elif d100_roll == 83:
        return "Ioun stone (strength)"
    elif d100_roll == 84:
        return "Armor, +2 leather"
    elif d100_roll == 85:
        return "Manual of bodily health"
    elif d100_roll == 86:
        return "Manual of gainful exercise"
    elif d100_roll == 87:
        return "Manual of golems"
    elif d100_roll == 88:
        return "Manual of quickness of action"
    elif d100_roll == 89:
        return "Mirror of life trapping"
    elif d100_roll == 90:
        return "Nine lives stealer"
    elif d100_roll == 91:
        return "Oathbow"
    elif d100_roll == 92:
        return "Armor, +2 scale mail"
    elif d100_roll == 93:
        return "Spellguard shield"
    elif d100_roll == 94:
        return "Armor, +1 splint"
    elif d100_roll == 95:
        return "Armor of resistance (splint)"
    elif d100_roll == 96:
        return "Armor, +1 studded leather"
    elif d100_roll == 97:
        return "Armor of resistance (studded leather)"
    elif d100_roll == 98:
        return "Tome of clear thought"
    elif d100_roll == 99:
        return "Tome of leadership and influence"
    elif d100_roll == 100:
        return "Tome of understanding"
        
def roll_magic_item_table_i():
    d100_roll = random.randint(1, 100)
    
    if 1 <= d100_roll <= 5:
        return "Defender"
    elif 6 <= d100_roll <= 10:
        return "Hammer of thunderbolts"
    elif 11 <= d100_roll <= 15:
        return "Luck Blade"
    elif 16 <= d100_roll <= 20:
        return "Sword of answering"
    elif 21 <= d100_roll <= 23:
        return "Holy avenger"
    elif 24 <= d100_roll <= 26:
        return "Ring of djinni summoning"
    elif 27 <= d100_roll <= 29:
        return "Ring of invisibility"
    elif 30 <= d100_roll <= 32:
        return "Ring of spell turning"
    elif 33 <= d100_roll <= 35:
        return "Rod of lordly might"
    elif 36 <= d100_roll <= 38:
        return "Vorpal sword"
    elif 39 <= d100_roll <= 41:
        return "Belt of cloud giant strength"
    elif 42 <= d100_roll <= 43:
        return "Armor, +2 breastplate"
    elif 44 <= d100_roll <= 45:
        return "Armor, +3 chain mail"
    elif 46 <= d100_roll <= 47:
        return "Armor, +3 chain shirt"
    elif 48 <= d100_roll <= 49:
        return "Cloak of invisibility"
    elif 50 <= d100_roll <= 51:
        return "Crystal ball (legendary version)"
    elif 52 <= d100_roll <= 53:
        return "Armor, +1 half plate"
    elif 54 <= d100_roll <= 55:
        return "Iron flask"
    elif 56 <= d100_roll <= 57:
        return "Armor, +3 leather"
    elif 58 <= d100_roll <= 59:
        return "Armor, +1 plate"
    elif 60 <= d100_roll <= 61:
        return "Robe of the archmagi"
    elif 62 <= d100_roll <= 63:
        return "Rod of resurrection"
    elif 64 <= d100_roll <= 65:
        return "Armor, +1 scale mail"
    elif 66 <= d100_roll <= 67:
        return "Scarab of protection"
    elif 68 <= d100_roll <= 69:
        return "Armor, +2 splint"
    elif 70 <= d100_roll <= 71:
        return "Armor, +2 studded leather"
    elif 72 <= d100_roll <= 73:
        return "Well of many worlds"
    elif d100_roll == 74:
        return "Magic armor (roll d12)"
    elif d100_roll == 75:
        return "Apparatus of Kwalish"
    elif d100_roll == 76:
        return "Armor of invulnerability"
    elif d100_roll == 77:
        return "Belt of storm giant strength"
    elif d100_roll == 78:
        return "Cubic gate"
    elif d100_roll == 79:
        return "Deck of many things"
    elif d100_roll == 80:
        return "Efreeti chain"
    elif d100_roll == 81:
        return "Armor of resistance (half plate)"
    elif d100_roll == 82:
        return "Horn of Valhalla (iron)"
    elif d100_roll == 83:
        return "Instrument of the bards (Ollamh harp)"
    elif d100_roll == 84:
        return "Ioun stone (greater absorption)"
    elif d100_roll == 85:
        return "Ioun stone (mastery)"
    elif d100_roll == 86:
        return "Ioun stone (regeneration)"
    elif d100_roll == 87:
        return "Plate armor of etherealness"
    elif d100_roll == 88:
        return "Plate armor of resistance"
    elif d100_roll == 89:
        return "Ring of air elemental command"
    elif d100_roll == 90:
        return "Ring of earth elemental command"
    elif d100_roll == 91:
        return "Ring of fire elemental command"
    elif d100_roll == 92:
        return "Ring of three wishes"
    elif d100_roll == 93:
        return "Ring of water elemental command"
    elif d100_roll == 94:
        return "Sphere of annihilation"
    elif d100_roll == 95:
        return "Talisman of pure good"
    elif d100_roll == 96:
        return "Talisman of the sphere"
    elif d100_roll == 97:
        return "Talisman of ultimate evil"
    elif d100_roll == 98:
        return "Tome of the stilled tongue"
    elif d100_roll == 99:
        return "Tome of the stilled tongue"
    elif d100_roll == 100:
        return "Tome of the stilled tongue"