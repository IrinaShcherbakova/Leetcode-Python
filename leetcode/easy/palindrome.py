def isPalindrome(s):
    if len(s) <= 1:
        return True
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum():
            i += 1
            if i >= len(s):
                return True
        while not s[j].isalnum():
            j -= 1
            if j < 0:
                return True
        if s[i] != s[j]:
            return False
        if i == j:
            return True
        else:
            i += 1
            j -= 1
    return True


str = "aa"
print("res is %s" % isPalindrome(str))