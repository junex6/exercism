from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

NUMBER_CATEGORIES = {ONES, TWOS, THREES, FOURS, FIVES, SIXES}

def score(dice, category):
    # Ones through sixes
    if category in NUMBER_CATEGORIES:
        return dice.count(category) * category

    counts = Counter(dice)
    most_common = counts.most_common()

    # Full house
    if category == FULL_HOUSE:
        if len(most_common) == 2 and most_common[0][1] == 3:
            return sum(dice)
    
    # Four of a kind
    if category == FOUR_OF_A_KIND:
        if (len(most_common) == 2 and most_common[0][1] == 4) or len(counts) == 1:
            return most_common[0][0] * 4

    # Little straight
    if category == LITTLE_STRAIGHT:
        if is_straight(dice) and min(dice) == 1:
            return 30
            
    # Big straight
    if category == BIG_STRAIGHT:
        if is_straight(dice) and min(dice) != 1:
            return 30

    # Choice
    if category == CHOICE:
        return sum(dice)

    # Yacht
    if category == YACHT and len(counts) == 1:
        return 50

    # Default fallback if no matches
    return 0

def is_straight(dice):
    return (
        len(dice) == len(set(dice)) and 
        max(dice) - min(dice) + 1 == len(dice)
    )
