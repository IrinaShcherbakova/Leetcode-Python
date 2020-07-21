class Solution:
    def intToRoman(self, n: int) -> str:
        res = ""
        if n // 1000 > 0:
            rem = n // 1000
            res = rem * 'M'
            n = n - (rem*1000)
        if n // 900 > 0:
            res += ('CM')
            n -= 900
        if n // 500 > 0:
            res += 'D'
            n -= 500
        if n // 400 > 0:
            res += ('CD')
            n -= 400
        if n // 100 > 0:
            rem = n // 100
            res += (rem * 'C')
            n = n - (rem*100)
        if n // 90 > 0:
            res += ('XC')
            n -= 90
        if n // 50 > 0:
            res += ('L')
            n -= 50
        if n // 40 > 0:
            res += ('XL')
            n -= 40
        if n // 10 > 0:
            rem = n // 10
            res += ('X'*rem)
            n -= (rem*10)
        if n // 9 > 0:
            res += ('IX')
            n -= 9
        if n // 5 > 0:
            res += ('V')
            n -= 5
        if n // 4 > 0:
            res += ('IV')
            n -= 4
        res += (n*'I')
        return res




   
            
            
            


            
