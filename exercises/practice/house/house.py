PARTS = [
    "house that Jack built.",
    "malt that lay in the",
    "rat that ate the",
    "cat that killed the",
    "dog that worried the",
    "cow with the crumpled horn that tossed the",
    "maiden all forlorn that milked the",
    "man all tattered and torn that kissed the",
    "priest all shaven and shorn that married the",
    "rooster that crowed in the morn that woke the",
    "farmer sowing his corn that kept the",
    "horse and the hound and the horn that belonged to the",
]


def verse(n):
    """Generate a single verse n (1-indexed)"""
    return f"This is the {' '.join(PARTS[n-1::-1])}"

    
def recite(start_verse, end_verse):
    """Generate a list of verses from start_verse to end_verse (1-indexed)"""
    return [verse(i) for i in range(start_verse, end_verse + 1)]
