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

def value(colors):
    return COLOR_CODE.index(colors[0]) * 10 + COLOR_CODE.index(colors[1])
