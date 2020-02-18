#with string conversion
# def isPalindrome(x):
#     if x < 0:
#         return False
#     forwardStr = str(x)
#     backwardStr = forwardStr[::-1]
#     if forwardStr == backwardStr:
#         return True
#     return False

#without string conversion
def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    reverseNumber = 0
    while x > reverseNumber:
        reverseNumber = reverseNumber * 10 + (x % 10)
        x //= 10
    if x == reverseNumber or x == reverseNumber//10:
        return True
    return False


print("res is %s" % isPalindrome(10))