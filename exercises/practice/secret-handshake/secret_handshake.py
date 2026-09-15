ACTIONS = [
    "wink",
    "double blink",
    "close your eyes",
    "jump",
]

def commands(binary_str):
    bits = binary_str.zfill(5)
    actions = [ACTIONS[i] for i, bit in enumerate(reversed(bits[-4:])) if bit == "1"]
    return actions[::-1] if bits[0] == "1" else actions
