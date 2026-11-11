import string

class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"

    @staticmethod
    def _clean(num):
        if any(c in string.ascii_letters for c in num):
            raise ValueError("letters not permitted")

        allowed_punc = "+()-. "
        if any(c in string.punctuation and c not in allowed_punc for c in num):
            raise ValueError("punctuations not permitted")
            
        table = str.maketrans("", "", allowed_punc)
        clean_num = num.translate(table)
        
        if len(clean_num) < 10: 
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_num) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        if len(clean_num) == 11:
            if clean_num[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean_num = clean_num[1:]
            
        if clean_num[0] == "0":
            raise ValueError("area code cannot start with zero")
        if clean_num[0] == "1":
            raise ValueError("area code cannot start with one")
            
        if clean_num[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if clean_num[3] == "1":
            raise ValueError("exchange code cannot start with one")
            
        return clean_num
