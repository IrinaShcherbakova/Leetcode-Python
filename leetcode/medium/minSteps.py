class Solution:
    def minSteps(self, s: str, t: str) -> int:
        one = [0] * 26
        two = [0] * 26
        for char in s:
            ind = ord(char) - 97
            one[ind] += 1
        for char in t:
            ind = ord(char) - 97
            two[ind] += 1
        count = 0
        for i in range(len(two)):
            two[i] = (0 if one[i] > two[i] else two[i] - one[i])
            count += two[i]
        return count
