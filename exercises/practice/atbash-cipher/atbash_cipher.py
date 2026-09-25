PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"
TRANS_MAP = str.maketrans(PLAIN, CIPHER)


def encode(plain_text):
    clean_text = "".join(char for char in plain_text.lower() if char.isalnum())
    translated = clean_text.translate(TRANS_MAP)
    return " ".join(translated[i:i + 5] for i in range(0, len(translated), 5))
 

def decode(ciphered_text):
    clean_text = "".join(ciphered_text.lower().split())
    return clean_text.translate(TRANS_MAP)
