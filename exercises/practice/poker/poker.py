from collections import Counter

ROYAL_FLUSH = 10
STRAIGHT_FLUSH = 9
FOUR_OF_A_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

RANK_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def best_hands(hands):
    ranked = [(hand, _hand_rank(hand)) for hand in hands]
    top_score = max(score for _, score in ranked)
    return [hand for hand, score in ranked if score == top_score]

def _split_hand(hand):
    ranks = []
    suits = []
    for card in hand.split():
        rank_str, suit = card[:-1], card[-1]
        ranks.append(RANK_MAP[rank_str])
        suits.append(suit)
        
    if set(ranks) == {14, 2, 3, 4, 5}:
        ranks = [1 if r == 14 else r for r in ranks]
    
    return ranks, suits

def _hand_rank(hand):
    ranks, suits = _split_hand(hand)
    is_straight = _is_straight(ranks)
    is_flush = _is_flush(suits)
    sorted_desc = sorted(ranks, reverse=True)

    if is_straight and is_flush:
        if 14 in ranks:
            return (ROYAL_FLUSH, *sorted_desc)
        return (STRAIGHT_FLUSH, *sorted_desc)

    ordered = sorted(
        Counter(ranks).items(),
        key=lambda item: (item[1], item[0]),
        reverse = True,
    )
    freq_pattern = [count for _, count in ordered]
    tie_breaker = [rank for rank, _ in ordered]
    
    if freq_pattern[0] == 4:
        return (FOUR_OF_A_KIND, *tie_breaker)
    if freq_pattern[:2] == [3, 2]:
        return (FULL_HOUSE, *tie_breaker)
    if is_flush:
        return (FLUSH, *sorted_desc)
    if is_straight:
        return (STRAIGHT, *sorted_desc)
    if freq_pattern[0] == 3:
        return (THREE_OF_A_KIND, *tie_breaker)
    if freq_pattern[:2] == [2, 2]:
        return (TWO_PAIR, *tie_breaker)
    if freq_pattern[0] == 2:
        return (ONE_PAIR, *tie_breaker)
    return (HIGH_CARD, *sorted_desc)

def _is_straight(ranks):
    return len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4

def _is_flush(suits):
    return len(set(suits)) == 1
