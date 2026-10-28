NTH = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

GIFT = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]

def _verse(n):
    intro = f"On the {NTH[n]} day of Christmas my true love gave to me: "
    
    if n == 1:
        return f"{intro}{GIFT[0]}."
    return f"{intro}{', '.join(GIFT[n-1:0:-1])}, and {GIFT[0]}."

def recite(start_verse, end_verse):
    return [_verse(i) for i in range(start_verse, end_verse+1)]
