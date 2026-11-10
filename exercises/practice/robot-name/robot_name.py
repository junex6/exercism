import random
import string

NAMES = set()

def generate_name():
    return "".join(
        random.choice(string.ascii_uppercase) for _ in range(2)
    ) + "".join(
        random.choice(string.digits) for _ in range(3)
    )

class Robot:
    
    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        name = generate_name()
        while name in NAMES:
            name = generate_name()
        NAMES.add(name)
        return name

    def reset(self):
        self.name = self._generate_name()
