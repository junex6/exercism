def abbreviate(words):
    words_clean = words.replace("-", " ").replace("_", " ")
    return "".join(word[0].upper() for word in words_clean.split())
