KNOWN_OPERATIONS = ["plus", "minus", "multiplied", "divided"]

def answer(question):
    tokens = _clean(question)

    max_len = len(tokens)
    if max_len == 1:
        return tokens[0]

    answer = tokens[0]
    for i in range(0, max_len, 2):
        if i+2 < max_len:
            if tokens[i+1] == "plus":
                answer += tokens[i+2]
            if tokens[i+1] == "minus":
                answer -= tokens[i+2]
            if tokens[i+1] == "multiplied":
                answer *= tokens[i+2]
            if tokens[i+1] == "divided":
                answer /= tokens[i+2]

    return answer

def _clean(question):
    # strip unnecessary words and question mark
    tokens = question.replace("What is ", "").replace("by ", "").replace("?", "").split()

    # check for errors
    for idx, token in enumerate(tokens):
        if idx % 2 == 0:
            try:
                tokens[idx] = int(tokens[idx])
            except ValueError:
                raise ValueError("syntax error")
        else:
            if not token.isalpha():
                raise ValueError("syntax error")
            if token not in KNOWN_OPERATIONS:
                raise ValueError("unknown operation")
    if len(tokens) % 2 != 1:
        raise ValueError("syntax error")
        
    return tokens
