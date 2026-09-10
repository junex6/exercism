def response(hey_bob):
    text = hey_bob.strip()

    isyelling = text.isupper()
    isquestion = text.endswith('?')
    
    if not text:
        return 'Fine. Be that way!'
    if isyelling and isquestion:
        return 'Calm down, I know what I\'m doing!'
    if isquestion:
        return 'Sure.'
    if isyelling:
        return 'Whoa, chill out!'
    
    return 'Whatever.'
