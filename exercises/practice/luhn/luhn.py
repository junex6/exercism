class Luhn:
    def __init__(self, card_num):
        self.num = "".join(card_num.split())

    def valid(self):
        if len(self.num) <= 1 or not self.num.isdigit():
            return False

        total = 0
        for i, n in enumerate(reversed(self.num)):
            digit = int(n)
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        return total % 10 == 0
