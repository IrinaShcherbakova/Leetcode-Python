def solution(s):
    res = ""
    for letter in s:
        if letter.islower():
            res += letter
        else:
            res = res + " " + letter
    return res


print("res is %s" % solution("helloWorld"))