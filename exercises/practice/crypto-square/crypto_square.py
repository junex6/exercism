from itertools import zip_longest
import string
import math

STRIP_TABLE = str.maketrans("", "", string.punctuation + string.whitespace)

def cipher_text(plain_text):
    clean_text = plain_text.lower().translate(STRIP_TABLE)
    if not clean_text:
        return ""
    
    cols = math.ceil(math.sqrt(len(clean_text)))
    rows = [clean_text[i:i+cols] for i in range(0, len(clean_text), cols)]
    columns = ["".join(c) for c in zip_longest(*rows, fillvalue=" ")]

    return " ".join(columns)
