def is_valid(isbn):
    isbn_clean = isbn.replace("-", "")

    if len(isbn_clean) != 10:
        return False
    
    total = 0
    
    for i, digit in enumerate(isbn_clean):
        if digit == "X" and i == 9:
            num = 10
        elif digit.isdigit():
            num = int(digit)
        else:
            return False
        total += num * (10 - i)
        
    return total % 11 == 0
