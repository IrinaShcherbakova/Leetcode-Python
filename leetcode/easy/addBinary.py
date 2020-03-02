def addBinary(a, b):
    res = shorterStr = longerStr = ""
    carry = length = 0
    if len(a) > len(b):
        longerStr = a
        shorterStr = b
    else:
        longerStr = b
        shorterStr = a
    i = len(longerStr) - 1
    j = len(shorterStr) - 1
    while j >= 0:
        if longerStr[i] == '1' and shorterStr[j] == '1':
            if carry >= 1:
                res = res + '1'
            else:
                carry += 1
                res = res + '0'
        elif longerStr[i] == '0' and shorterStr[j] == '0':
            if carry >= 1:
                res = res + '1'
                carry -= 1
            else:
                res = res + '0'
        elif longerStr[i] == '1' or shorterStr[j] == '1':
            if carry >= 1:
                res = res + '0'
            else:
                res = res + '1'
        i -= 1
        j -= 1
    #copy the rest of the longer string
    while i >= 0:
        if longerStr[i] == '1':
            if carry >= 1:
                res = res + '0'
            else:
                res = res + '1'
        else:
            if carry >= 1:
                carry -= 1
                res = res + '1'
            else:
                res = res + '0'
        i -= 1
    while carry > 0:
        res = res + '1'
        carry -= 1
    return res[::-1]


a = "110010"
b = "10111"
print("res is %s" % addBinary(a, b))