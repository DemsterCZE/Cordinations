cislice = ["0","1","2","3","4","5","6","7","8","9"]

def to_roman(num):
    try:
        num = int(num)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i, value in enumerate(values):
            while num >= value:
                roman += symbols[i]
                num -= value
        return roman
    except ValueError:
        return num


def find_numbers_before_ulice(string):
    word_list = string.split()
    for i, word in enumerate(word_list):
        if word == "ulice":
            if i > 0 and word_list[i-1].isdigit():
                return str(word_list[i-1])
            else:
                return string
            