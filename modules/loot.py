import random
from magic_tables import *
from gem_tables import *
from art_tables import *

def generate_treasure_cr_0_4(d100_roll):
    treasure = {
        "CP": 0,
        "SP": 0,
        "EP": 0,
        "GP": 0,
        "PP": 0
    }
    
    if 1 <= d100_roll <= 30:
        treasure["CP"] = sum(random.randint(1, 6) for _ in range(5))
    elif 31 <= d100_roll <= 60:
        treasure["SP"] = sum(random.randint(1, 6) for _ in range(4))
    elif 61 <= d100_roll <= 70:
        treasure["EP"] = sum(random.randint(1, 6) for _ in range(3))
    elif 71 <= d100_roll <= 95:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(3))
    elif 96 <= d100_roll <= 100:
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(1))
    
    return treasure
   
def generate_treasure_cr_5_10(d100_roll):
    treasure = {
        "CP": 0,
        "SP": 0,
        "EP": 0,
        "GP": 0,
        "PP": 0
    }
    
    if 1 <= d100_roll <= 30:
        treasure["CP"] = sum(random.randint(1, 6) for _ in range(4)) * 100
        treasure["EP"] = sum(random.randint(1, 6) for _ in range(1)) * 10
    elif 31 <= d100_roll <= 60:
        treasure["SP"] = sum(random.randint(1, 6) for _ in range(6)) * 10
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(2)) * 10
    elif 61 <= d100_roll <= 70:
        treasure["EP"] = sum(random.randint(1, 6) for _ in range(1)) * 100
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(2)) * 10
    elif 71 <= d100_roll <= 95:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(4)) * 10
    elif 96 <= d100_roll <= 100:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(2)) * 10
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(3))
    
    return treasure
    
def generate_treasure_cr_11_16(d100_roll):
    treasure = {
        "CP": 0,
        "SP": 0,
        "EP": 0,
        "GP": 0,
        "PP": 0
    }
    
    if 1 <= d100_roll <= 20:
        treasure["SP"] = sum(random.randint(1, 6) for _ in range(4)) * 100
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(1)) * 100
    elif 21 <= d100_roll <= 35:
        treasure["EP"] = sum(random.randint(1, 6) for _ in range(1)) * 100
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(1)) * 100
    elif 36 <= d100_roll <= 75:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(2)) * 100
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(1)) * 10
    elif 76 <= d100_roll <= 100:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(2)) * 100
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(2)) * 10
    
    return treasure
    
import random

def generate_treasure_cr_17_plus(d100_roll):
    treasure = {
        "CP": 0,
        "SP": 0,
        "EP": 0,
        "GP": 0,
        "PP": 0
    }
    
    if 1 <= d100_roll <= 15:
        treasure["EP"] = sum(random.randint(1, 6) for _ in range(2)) * 1000
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(8)) * 100
    elif 16 <= d100_roll <= 55:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(1)) * 1000
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(1)) * 100
    elif 56 <= d100_roll <= 100:
        treasure["GP"] = sum(random.randint(1, 6) for _ in range(1)) * 1000
        treasure["PP"] = sum(random.randint(1, 6) for _ in range(2)) * 100
    
    return treasure


def roll_treasure_hoard_cr_0_4():
    # Roll for coins
    cp = random.randint(1, 6) * 100
    sp = random.randint(1, 3) * 100
    ep = 0
    gp = random.randint(1, 2) * 10
    pp = 0
    
    # Roll for gems or art objects
    gems_or_art_objects_roll = random.randint(1, 100)
    gems = []
    art_objects = []
    magic_items = []
    
    # Determine gems or art objects
    if 1 <= gems_or_art_objects_roll <= 6:
        pass  # No gems or art objects
    elif 7 <= gems_or_art_objects_roll <= 16:
        gems = [roll_10_gp_gemstone() for _ in range(random.randint(2, 6))]
    elif 17 <= gems_or_art_objects_roll <= 26:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
    elif 27 <= gems_or_art_objects_roll <= 36:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
    elif 37 <= gems_or_art_objects_roll <= 44:
        gems = [roll_10_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 45 <= gems_or_art_objects_roll <= 52:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 53 <= gems_or_art_objects_roll <= 60:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 61 <= gems_or_art_objects_roll <= 65:
        gems = [roll_10_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 66 <= gems_or_art_objects_roll <= 70:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 71 <= gems_or_art_objects_roll <= 75:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 76 <= gems_or_art_objects_roll <= 78:
        gems = [roll_10_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 79 <= gems_or_art_objects_roll <= 80:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 81 <= gems_or_art_objects_roll <= 85:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 86 <= gems_or_art_objects_roll <= 92:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 93 <= gems_or_art_objects_roll <= 97:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 98 <= gems_or_art_objects_roll <= 99:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_g())
    elif gems_or_art_objects_roll == 100:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(2, 6))]
        magic_items.append(roll_magic_item_table_g())
        
    return {
        "CP": cp,
        "SP": sp,
        "EP": ep,
        "GP": gp,
        "PP": pp,
        "Gems": gems,
        "Art Objects": art_objects,
        "Magic Items": magic_items
    }
        

def roll_treasure_hoard_cr_5_10():
    # Roll for coins
    cp = random.randint(1, 6) * 100
    sp = random.randint(1, 6) * 1000
    ep = 0
    gp = random.randint(1, 6) * 100
    pp = random.randint(1, 3) * 10
    
    # Roll for gems or art objects
    gems_or_art_objects_roll = random.randint(1, 100)
    gems = []
    art_objects = []
    magic_items = []
    
    # Determine gems or art objects
    if 1 <= gems_or_art_objects_roll <= 4:
        pass  # No gems or art objects
    elif 5 <= gems_or_art_objects_roll <= 10:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
    elif 11 <= gems_or_art_objects_roll <= 16:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
    elif 17 <= gems_or_art_objects_roll <= 22:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
    elif 23 <= gems_or_art_objects_roll <= 28:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
    elif 29 <= gems_or_art_objects_roll <= 32:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 33 <= gems_or_art_objects_roll <= 36:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 37 <= gems_or_art_objects_roll <= 40:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 41 <= gems_or_art_objects_roll <= 44:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 6))])
    elif 45 <= gems_or_art_objects_roll <= 49:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 50 <= gems_or_art_objects_roll <= 54:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 55 <= gems_or_art_objects_roll <= 59:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 60 <= gems_or_art_objects_roll <= 63:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 4))])
    elif 64 <= gems_or_art_objects_roll <= 66:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 67 <= gems_or_art_objects_roll <= 69:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 70 <= gems_or_art_objects_roll <= 72:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 73 <= gems_or_art_objects_roll <= 74:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 4))])
    elif 75 <= gems_or_art_objects_roll <= 76:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_d())
    elif 77 <= gems_or_art_objects_roll <= 78:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_d())
    elif 79 <= gems_or_art_objects_roll <= 79:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
        magic_items.append(roll_magic_item_table_d())
    elif 80 <= gems_or_art_objects_roll <= 80:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_d())
    elif 81 <= gems_or_art_objects_roll <= 84:
        art_objects = [roll_25_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 85 <= gems_or_art_objects_roll <= 88:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 89 <= gems_or_art_objects_roll <= 91:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 92 <= gems_or_art_objects_roll <= 94:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(random.randint(1, 4))])
    elif 95 <= gems_or_art_objects_roll <= 96:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 4))])
    elif 97 <= gems_or_art_objects_roll <= 98:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 6))])
    elif 99 <= gems_or_art_objects_roll <= 99:
        gems = [roll_50_gp_gemstone() for _ in range(random.randint(6, 12))]
        magic_items.append(roll_magic_item_table_h())
    elif gems_or_art_objects_roll == 100:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_h())
    
    return {
        "CP": cp,
        "SP": sp,
        "EP": ep,
        "GP": gp,
        "PP": pp,
        "Gems": gems,
        "Art Objects": art_objects,
        "Magic Items": magic_items
    }

def roll_treasure_hoard_cr_11_16():
    # Roll for coins
    cp = 0
    sp = 0
    ep = 0
    gp = random.randint(1, 6) * 1000
    pp = random.randint(1, 6) * 100
    
    # Roll for gems or art objects
    gems_or_art_objects_roll = random.randint(1, 100)
    gems = []
    art_objects = []
    magic_items = []
    
    # Determine gems or art objects
    if 1 <= gems_or_art_objects_roll <= 3:
        pass  # No gems or art objects
    elif 4 <= gems_or_art_objects_roll <= 6:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
    elif 7 <= gems_or_art_objects_roll <= 10:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
    elif 11 <= gems_or_art_objects_roll <= 12:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
    elif 13 <= gems_or_art_objects_roll <= 15:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
    elif 16 <= gems_or_art_objects_roll <= 19:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 4))])
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 6))])
    elif 20 <= gems_or_art_objects_roll <= 23:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 4))])
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 6))])
    elif 24 <= gems_or_art_objects_roll <= 26:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 4))])
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 6))])
    elif 27 <= gems_or_art_objects_roll <= 29:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_a() for _ in range(random.randint(1, 4))])
        magic_items.extend([roll_magic_item_table_b() for _ in range(random.randint(1, 6))])
    elif 30 <= gems_or_art_objects_roll <= 35:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 6))])
    elif 36 <= gems_or_art_objects_roll <= 40:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 6))])
    elif 41 <= gems_or_art_objects_roll <= 45:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 6))])
    elif 46 <= gems_or_art_objects_roll <= 50:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_c() for _ in range(random.randint(1, 6))])
    elif 51 <= gems_or_art_objects_roll <= 54:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_d() for _ in range(random.randint(1, 4))])
    elif 55 <= gems_or_art_objects_roll <= 58:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_d() for _ in range(random.randint(1, 4))])
    elif 59 <= gems_or_art_objects_roll <= 62:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_d() for _ in range(random.randint(1, 4))])
    elif 63 <= gems_or_art_objects_roll <= 66:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_d() for _ in range(random.randint(1, 4))])
    elif 67 <= gems_or_art_objects_roll <= 68:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_e())
    elif 69 <= gems_or_art_objects_roll <= 70:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_e())
    elif 71 <= gems_or_art_objects_roll <= 72:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_e())
    elif 73 <= gems_or_art_objects_roll <= 74:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_e())
    elif 75 <= gems_or_art_objects_roll <= 76:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(1)])
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 4))])
    elif 77 <= gems_or_art_objects_roll <= 78:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(1)])
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 4))])
    elif 79 <= gems_or_art_objects_roll <= 80:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(1)])
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 4))])
    elif 81 <= gems_or_art_objects_roll <= 82:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_f() for _ in range(1)])
        magic_items.extend([roll_magic_item_table_g() for _ in range(random.randint(1, 4))])
    elif 83 <= gems_or_art_objects_roll <= 85:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_h() for _ in range(random.randint(1, 4))])
    elif 86 <= gems_or_art_objects_roll <= 88:
        art_objects = [roll_750_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.extend([roll_magic_item_table_h() for _ in range(random.randint(1, 4))])
    elif 89 <= gems_or_art_objects_roll <= 90:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_h() for _ in range(random.randint(1, 4))])
    elif 91 <= gems_or_art_objects_roll <= 92:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.extend([roll_magic_item_table_h() for _ in range(random.randint(1, 4))])
    elif 93 <= gems_or_art_objects_roll <= 94:
        art_objects = [roll_250_gp_art_object() for _ in range(random.randint(2, 4))]
        magic_items.append(roll_magic_item_table_i())
    elif 95 <= gems_or_art_objects_roll <= 96:
        gems = [roll_500_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_i())
    elif 97 <= gems_or_art_objects_roll <= 98:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_i())
    elif 99 <= gems_or_art_objects_roll <= 100:
        gems = [roll_1000_gp_gemstone() for _ in range(random.randint(3, 6))]
        magic_items.append(roll_magic_item_table_i())
    
    return {
        "CP": cp,
        "SP": sp,
        "EP": ep,
        "GP": gp,
        "PP": pp,
        "Gems": gems,
        "Art Objects": art_objects,
        "Magic Items": magic_items
    }
hoard = roll_treasure_hoard_cr_11_16()
print(hoard)