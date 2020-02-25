# Given a string s consists of upper/lower-case alphabets and
# empty space characters ' ', return the length of last word
# (last word means the last appearing word if we loop from left to right)
# in the string. If the last word does not exist, return 0.

def lengthOfLastWord(s):
    strings = s.split(" ")
    for string in strings[::-1]:
        if len(string) > 0:
            return len(string)
    return 0


print("res is %s" % lengthOfLastWord("a "))