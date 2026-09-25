def rows(letter):
    alphabet = [chr(i) for i in range(ord("A"), ord(letter) + 1)]
    width = len(alphabet) * 2 - 1
    top_half = []
    
    for i, char in enumerate(alphabet):
        if char == "A":
            row = "A".center(width)
        else:
            inner_spaces = " " * (2 * i - 1)
            row = f"{char}{inner_spaces}{char}".center(width)
        top_half.append(row)

    return top_half + top_half[-2::-1]
