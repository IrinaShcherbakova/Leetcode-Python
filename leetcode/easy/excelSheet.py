def convertToTitle(self, n: int) -> str:
    shift = 64
    res = ""
    reminder = []
    while n > 0:
        reminder = divmod(n, 26)
        if reminder[1] == 0:
            newRemainder = []
            newRemainder.append(reminder[0] - 1)
            newRemainder.append(26)
            reminder = newRemainder
        res = chr(reminder[1] + shift) + res
        n = reminder[0]
    return res
