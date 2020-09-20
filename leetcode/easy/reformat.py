class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        digits = []
        for char in s:
            if char.isalpha():
                chars.append(char)
            else:
                digits.append(char)
        if abs(len(chars) - len(digits)) > 1:
            return ""
        first = (chars if len(chars) >= len(digits) else digits)
        second = (chars if len(chars) < len(digits) else digits)
        res = []
        j = 0
        for i in range(len(first)-1):
            res.append(first[i])
            res.append(second[j])
            j += 1
        res.append(first[-1])
        if j < len(second):
            res.append(second[j])
        return "".join(res)
