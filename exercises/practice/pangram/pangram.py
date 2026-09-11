def is_pangram(sentence):
    letters = "".join([char for char in sentence if char.isalpha()])
    return len(set(letters.lower())) == 26
