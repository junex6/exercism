import re

def decode(string):

    return "".join(
        char * int(num or 1) 
        for num, char in re.findall(r"(\d*)(\D)", string)
    )


def encode(string):

    return "".join(
        f"{len(m.group(0))}{m.group(1)}" 
        if len(m.group(0)) > 1 else m.group(1) 
        for m in re.finditer(r"(.)\1*", string)
    )
