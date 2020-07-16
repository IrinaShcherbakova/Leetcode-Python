class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        operations = []
        res = x
        power = abs(n)
        #we create an addition chain of n based on its binary representation.
        #True means double power of result
        #False means add 1 to a power of result
        while power != 0:
            bit = power & 1
            if bit == 0:
                operations.append(True)
            else:
                operations.append(False)
                operations.append(True)
            power >>=1
        #remove the first 1
        operations.pop()
        operations.pop()
        while len(operations) > 0:
            cur = operations.pop()
            if cur:
                res *= res
            else:
                res *= x
        if n < 0:
            return 1 / res
        return res
