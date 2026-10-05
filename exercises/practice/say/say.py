MAPPING = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

SCALES = (
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand"),
)

def _three_digits_to_words(number: int) -> str:
    """Converts a number from 1 to 999 into words."""
    parts = []

    hundreds, rem = divmod(number, 100)
    if hundreds:
        parts.append(f"{MAPPING[hundreds]} hundred")
        
    if rem in MAPPING:
        parts.append(MAPPING[rem])
    elif rem > 0:
        tens, ones = divmod(rem, 10)
        parts.append(f"{MAPPING[tens * 10]}-{MAPPING[ones]}")
        
    return " ".join(parts)


def say(number):
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    chunks = [
        (number // 1_000_000_000, "billion"),
        (number % 1_000_000_000 // 1_000_000, "million"),
        (number % 1_000_000 // 1_000, "thousand"),
        (number % 1_000, ""),
    ]

    words = []

    for scale, label in SCALES:
        chunk, number = divmod(number, scale)
        if chunk:
            words.append(f"{_three_digits_to_words(chunk)} {label}")

    if number:
        words.append(_three_digits_to_words(number))
    return " ".join(words)
