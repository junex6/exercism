_LETTER_GROUPS = {
    1: "AEIOULNRST",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

SCORES = {
    char: score
    for score, letters in _LETTER_GROUPS.items()
    for char in letters
}

def score(word):
    return sum(SCORES.get(char, 0) for char in word.upper())
