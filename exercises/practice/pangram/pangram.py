def is_pangram(sentence):
    letters = [char.lower() for char in sentence if char.isalpha()]
    return len(set(letters)) == 26
