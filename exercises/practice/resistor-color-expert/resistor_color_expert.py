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

TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    tolerance = TOLERANCE[colors[-1]]
    exponent = COLOR_CODE.index(colors[-2])

    base_digits = [str(COLOR_CODE.index(color)) for color in colors[:-2]]
    base_num = int("".join(base_digits))

    number = base_num * (10 ** exponent)
    
    prefixes = ["", "kilo", "mega", "giga"]
    prefix_idx = 0

    while number >= 1000 and prefix_idx < len(prefixes) - 1:             
        number /= 1000
        prefix_idx += 1

    if number.is_integer():
        number = int(number)
    
    return f"{number} {prefixes[prefix_idx]}ohms ±{tolerance}%"
