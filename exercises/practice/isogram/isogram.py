def is_isogram(phrase):
    clean_phrase = [char.lower() for char in phrase if char.isalpha()]
    return len(set(clean_phrase)) == len(clean_phrase)
