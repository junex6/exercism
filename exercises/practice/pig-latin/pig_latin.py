import re

PATTERN_VOWEL = re.compile(r"^(a|e|i|o|u|xr|yt)")
PATTERN_CONSONANT = re.compile(r"^([bcdfghjklmnpqrstvwxyz]+)(.*)$")
PATTERN_QU = re.compile(r"^([bcdfghjklmnpqrstvwxyz]*qu)(.*)$")
PATTERN_Y = re.compile(r"^([bcdfghjklmnpqrstvwxyz]+)(y.*)$")

def translate(text):
    return " ".join(piglatin(word) for word in text.split())

def piglatin(word):
    if PATTERN_VOWEL.match(word):
        return f"{word}ay"
    if match := PATTERN_QU.match(word):
        return f"{match.group(2)}{match.group(1)}ay"
    if match := PATTERN_Y.match(word):
        return f"{match.group(2)}{match.group(1)}ay"
    if match := PATTERN_CONSONANT.match(word):
        return f"{match.group(2)}{match.group(1)}ay"
    return word
