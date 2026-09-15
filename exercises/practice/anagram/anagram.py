def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    
    return [c for c in candidates 
            if word_lower != (c_lower := c.lower())
            and word_sorted == sorted(c_lower)]
