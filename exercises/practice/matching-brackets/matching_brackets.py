def is_paired(input_string):
    mapping = {"]":"[", "}":"{", ")":"("}
    stack = []
    
    for char in input_string:
        if char in mapping.values():
            stack.append(char)
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0
