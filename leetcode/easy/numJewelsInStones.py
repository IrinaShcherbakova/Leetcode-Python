class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for char in S:
            if char in J:
                counter += 1
        return counter
