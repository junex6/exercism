# def roman(number):
#     thousands = number // 1000
#     hundreds = (number - thousands * 1000) // 100
#     tens = (number - thousands * 1000 - hundreds * 100) // 10
#     ones = number - thousands * 1000 - hundreds * 100 - tens * 10

#     roman_num = str()

#     # thousands
#     roman_num += thousands * "M"

#     # hundreds
#     if hundreds < 4:
#         roman_num += hundreds * "C"
#     elif hundreds == 4: 
#         roman_num += "CD"
#     elif 4 < hundreds < 9:
#         roman_num += "D" + (hundreds - 5) * "C"
#     elif hundreds == 9:
#         roman_num += "CM"

#     # tens
#     if tens < 4:
#         roman_num += tens * "X"
#     elif tens == 4:
#         roman_num += "XL"
#     elif 4 < tens < 9:
#         roman_num += "L" + (tens - 5) * "X"
#     elif tens == 9:
#         roman_num += "XC"

#     # ones
#     if ones < 4:
#         roman_num += ones * "I"
#     elif ones == 4:
#         roman_num += "IV"
#     elif 4 < ones < 9:
#         roman_num += "V" + (ones - 5) * "I"
#     elif ones == 9:
#         roman_num += "IX"

#     return roman_num

def roman(number):
    # Lookup tables for each place value
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return (
        thousands[number // 1000] +
        hundreds[(number // 100) % 10] +
        tens[(number // 10) % 10] +
        ones[number % 10]
    )
