NUMBER_WORDS = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

def _bottle_phrase(n: int) -> str:
    noun = "bottle" if n == 1 else "bottles"
    return f"{NUMBER_WORDS[n]} green {noun} hanging on the wall"

def _verse(n: int) -> list[str]:
    opening = f"{_bottle_phrase(n).capitalize()},"
    closing = f"There'll be {_bottle_phrase(n - 1)}."
    return [opening, opening, "And if one green bottle should accidentally fall,", closing]

def recite(start: int, take: int = 1) -> list[str]:
    verses: list[str] = []
    for i, n in enumerate(range(start, start-take, -1)):
        if i > 0:
            verses.append("")
        verses.extend(_verse(n))
    return verses
