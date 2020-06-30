class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts = {}
        bulls, cows = 0, 0
        for i, num in enumerate(secret):
            if num == guess[i]:
                bulls += 1
                continue
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for i, num in enumerate(guess):
            if num != secret[i] and num in counts:
                cows += 1
                if counts[num] == 1:
                    counts.pop(num)
                else:
                    counts[num] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
                
                
