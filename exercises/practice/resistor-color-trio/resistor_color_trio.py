COLOR_CODE = [
    "black", 
    "brown", 
    "red", 
    "orange", 
    "yellow", 
    "green", 
    "blue", 
    "violet", 
    "grey", 
    "white"
]


def label(colors):
    base = COLOR_CODE.index(colors[0]) * 10 + COLOR_CODE.index(colors[1])
    exponents = COLOR_CODE.index(colors[2])
    number = base * (10 ** exponents)

    prefixes = ["", "kilo", "mega", "giga"]
    prefix_idx = 0

    while number > 0 and number % 1000 == 0 and prefix_idx < len(prefixes) - 1: 
        number //= 1000
        prefix_idx += 1
    
    return f"{number} {prefixes[prefix_idx]}ohms"
