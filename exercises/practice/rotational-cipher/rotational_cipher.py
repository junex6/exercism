def rotate(text, key):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    shifted_lower = lower[key:] + lower[:key]
    shifted_upper = upper[key:] + upper[:key]
    
    trans_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
    
    return text.translate(trans_table)
