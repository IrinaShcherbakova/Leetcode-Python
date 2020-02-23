# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    exceptions = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
    i = res = 0
    while i < len(s) - 1:
        doubleChar = s[i:i+2]
        if doubleChar in exceptions:
            res += exceptions[doubleChar]
            i += 2
            continue
        res += romans[s[i]]
        i += 1
    if i == len(s):
        return res
    else:
        return res + romans[s[i]]



print("res is %s" % romanToInt("IX"))