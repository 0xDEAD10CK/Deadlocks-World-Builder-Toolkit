import random

prefixes = [
    "Ael", "Bal", "Cor", "Dor", "Eld", "Fen", "Gal", "Hal", "Ith", "Jor", 
    "Kal", "Lor", "Mar", "Nel", "Or", "Pal", "Quin", "Ral", "Sar", "Tor", 
    "Ul", "Val", "Wyn", "Xar", "Yor", "Zal", "Ar", "Bran", "Cer", "Dran"
]


middles = [
    "a", "e", "i", "o", "u", "an", "en", "in", "on", "un", 
    "ar", "er", "ir", "or", "ur", "al", "el", "il", "ol", "ul", 
    "am", "em", "im", "om", "um", "ath", "eth", "ith", "oth", "uth", 
    "as", "es", "is", "os", "us", "an", "en", "in", "on", "un"
]

suffixes = [
    "dor", "fin", "gar", "hor", "kin", "lor", "mar", "nir", "or", "pin", 
    "quar", "rin", "sar", "tor", "var", "win", "xar", "yr", "zan", "nor", 
    "dral", "thal", "vyr", "dan", "gran", "rin", "tar", "vor", "zan", "yrr", 
    "dor", "fyr", "ghal", "mir", "nor", "ril", "sur", "ten", "val", "zar"
]


def gen_name():
    num = random.randint(2,3)

    if num == 2:
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        return prefix + suffix
    else:
        prefix = random.choice(prefixes)
        middle = random.choice(middles)
        suffix = random.choice(suffixes)

        return prefix + middle + suffix
