def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x = abs(x)
    reverseNum = str(x)
    reverseNum = reverseNum[::-1]
    reverseNum = int(reverseNum)
    if reverseNum > pow(2,31) - 1:
        return 0
    if negative:
        return -reverseNum
    return reverseNum



print("res is %s" % reverse(-153))