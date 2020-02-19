def longestCommonPrefix(strs):
    if len(strs) == 0 or strs[0] == "":
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        currentString = strs[i]
        if prefix == currentString:
            continue
        if len(currentString) < len(prefix):
            prefix = prefix[:len(currentString)]
        if len(currentString) == 0 or prefix[0] != currentString[0]:
            return ""
        for j in range(0, len(prefix)):
            if prefix[j] != currentString[j]:
                prefix = prefix[:j]
                break
    return prefix





print("res is %s" % longestCommonPrefix(["abab","aba",""]))