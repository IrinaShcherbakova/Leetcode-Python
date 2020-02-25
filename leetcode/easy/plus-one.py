# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer. The digits are stored such that
# the most significant digit is at the head of the list, and
# each element in the array contain a single digit. You may assume
# the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    targetInteger = 0
    for digit in digits:
        targetInteger = targetInteger * 10 + digit
    targetInteger += 1
    stringInteger = str(targetInteger)
    incrementedInteger = []
    for digit in stringInteger:
        incrementedInteger.append(int(digit))
    return incrementedInteger


print("res is %s" % plusOne([0]))

