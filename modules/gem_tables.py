import random

def roll_10_gp_gemstone():
    """Returns a 10 GP gemstone based on a d12 roll."""
    gemstones_10_gp = [
        "10gp: Azurite (opaque mottled deep blue)",
        "10gp: Banded agate (translucent striped brown, blue, white, or red)",
        "10gp: Blue quartz (transparent pale blue)",
        "10gp: Eye agate (translucent circles of gray, white, brown, blue, or green)",
        "10gp: Hematite (opaque gray-black)",
        "10gp: Lapis lazuli (opaque light and dark blue with yellow flecks)",
        "10gp: Malachite (opaque striated light and dark green)",
        "10gp: Moss agate (translucent pink or yellow-white with mossy gray or green markings)",
        "10gp: Obsidian (opaque black)",
        "10gp: Rhodochrosite (opaque light pink)",
        "10gp: Tiger eye (translucent brown with golden center)",
        "10gp: Turquoise (opaque light blue-green)"
    ]
    roll = random.randint(1, 12) - 1  # Roll a d12 (1-12) and adjust for 0-indexed list
    return gemstones_10_gp[roll]

def roll_50_gp_gemstone():
    """Returns a 50 GP gemstone based on a d12 roll."""
    gemstones_50_gp = [
        "50gp: Bloodstone (opaque dark gray with red flecks)",
        "50gp: Carnelian (opaque orange to red-brown)",
        "50gp: Chalcedony (opaque white)",
        "50gp: Chrysoprase (translucent green)",
        "50gp: Citrine (transparent pale yellow-brown)",
        "50gp: Jasper (opaque blue, black, or brown)",
        "50gp: Moonstone (translucent white with pale blue glow)",
        "50gp: Onyx (opaque bands of black and white, or pure black or white)",
        "50gp: Quartz (transparent white, smoky gray, or yellow)",
        "50gp: Sardonyx (opaque bands of red and white)",
        "50gp: Star rose quartz (translucent rosy stone with white star-shaped center)",
        "50gp: Zircon (transparent pale blue-green)"
    ]
    roll = random.randint(1, 12) - 1  # Roll a d12 (1-12) and adjust for 0-indexed list
    return gemstones_50_gp[roll]

def roll_500_gp_gemstone():
    """Returns a 500 GP gemstone based on a d6 roll."""
    gemstones_500_gp = [
        "500gp: Alexandrite (transparent dark green)",
        "500gp: Aquamarine (transparent pale blue-green)",
        "500gp: Black pearl (opaque pure black)",
        "500gp: Blue spinel (transparent deep blue)",
        "500gp: Peridot (transparent rich olive green)",
        "500gp: Topaz (transparent golden yellow)"
    ]
    roll = random.randint(1, 6) - 1  # Roll a d6 (1-6) and adjust for 0-indexed list
    return gemstones_500_gp[roll]

def roll_1000_gp_gemstone():
    """Returns a 1000 GP gemstone based on a d8 roll."""
    gemstones_1000_gp = [
        "1000gp: Black opal (translucent dark green with black mottling and golden flecks)",
        "1000gp: Blue sapphire (transparent blue-white to medium blue)",
        "1000gp: Emerald (transparent deep bright green)",
        "1000gp: Fire opal (translucent fiery red)",
        "1000gp: Opal (translucent pale blue with green and golden mottling)",
        "1000gp: Star ruby (translucent ruby with white star-shaped center)",
        "1000gp: Star sapphire (translucent blue sapphire with white star-shaped center)",
        "1000gp: Yellow sapphire (transparent fiery yellow or yellow green)"
    ]
    roll = random.randint(1, 8) - 1  # Roll a d8 (1-8) and adjust for 0-indexed list
    return gemstones_1000_gp[roll]
    
def roll_5000_gp_gemstone():
    """Returns a 5000 GP gemstone based on a d4 roll."""
    gemstones_5000_gp = [
        "5000gp: Black sapphire (translucent lustrous black with glowing highlights)",
        "5000gp: Diamond (transparent blue-white, canary, pink, brown, or blue)",
        "5000gp: Jacinth (transparent fiery orange)",
        "5000gp: Ruby (transparent clear red to deep crimson)"
    ]
    roll = random.randint(1, 4) - 1  # Roll a d4 (1-4) and adjust for 0-indexed list
    return gemstones_5000_gp[roll]