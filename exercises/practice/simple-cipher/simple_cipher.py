import random
import string
from itertools import cycle

LETTERS = list(string.ascii_lowercase)

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = "".join(random.choices(LETTERS, k=100))

        self.key = key
        self._key_idx = self._get_index(key)

    def encode(self, text):
        return self._transform(text, direction=1)

    def decode(self, text):
        return self._transform(text, direction=-1)

    def _transform(self, text, direction):
        text_idx = self._get_index(text)
        shifted = [
            LETTERS[(t_idx + direction * k_idx) % 26]
            for t_idx, k_idx in zip(text_idx, cycle(self._key_idx))
        ]
        return "".join(shifted)

    @staticmethod
    def _get_index(text):
        return [LETTERS.index(char) for char in text]
