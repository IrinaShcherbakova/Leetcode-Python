class Solution:
    def myAtoi(self, str: str) -> int:
        start = self.skipWhitespaces(str)
        if start < 0:
            return 0
        if (str[start] != '-') and (str[start] != '+') and (str[start] < '0' or str[start] > '9'):
            return 0
        start = (start + 1 if str[start] == '-' or str[start] == '+' else start)
        res = 0
        for i in range(start, len(str)):
            if (str[i] < '0' or str[i] > '9') and res > 0:
                break
            if (str[i] < '0' or str[i] > '9') and res == 0:
                return 0
            if str[i] >= '0' and str[i] <= '9':
                res = res * 10 + int(str[i])
                if res >= 2147483648:
                    return (2147483648 * -1 if start-1 >= 0 and str[start-1] == '-' else 2147483647)
        print("start is %s" %str[start-1])
        return (res * -1 if start-1 >= 0 and str[start-1] == '-' else res)
                    
    
    def skipWhitespaces(self, s: str) -> int:
        for i, char in enumerate(s):
            if char != ' ':
                return i
        return -1
        
