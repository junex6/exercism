"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_sublist(short_list, long_list):
    if not short_list:
        return True

    len_short = len(short_list)
    len_long = len(long_list)

    return any(short_list == long_list[i : (i+len_short)] for i in range(len_long - len_short + 1))


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
