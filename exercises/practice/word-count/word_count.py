import re
from collections import Counter

pattern = r"\b\w+(?:'\w+)?\b"

def count_words(sentence):
    cleaned = sentence.lower().replace("_", " ")
    words = re.findall(pattern, cleaned)
    return Counter(words)
