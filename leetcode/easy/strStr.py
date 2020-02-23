#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        needleLength = len(needle)
        for i in range(0, len(haystack) - needleLength + 1):
            if haystack[i:i+needleLength] == needle:
                return i
        return -1




print("res is %s" % strStr("aaaaa", "bba"))