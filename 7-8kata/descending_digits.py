from math import floor

def descending_order(num):
    sorted_string = sorted(str(num))
    reversed_string = sorted_string[::-1]
    res = ""
    for number in reversed_string:
        res += number
    return int(res)


def make_negative( number ):
    if number < 0:
        return number
    else:
        return number * (-1)


def litres(time):
    res = int(time * 0.5)
    return res


def square_digits(num):
    digits_str = "".join(str(num))
    res = []
    for digit in digits_str:
        res.append(int(digit)*int(digit))
    squared_num = ""
    for digit in res:
        squared_num += str(digit)
    return int(squared_num)

print("result is %s" % square_digits(9119))
