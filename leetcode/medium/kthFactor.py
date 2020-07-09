class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count, i = 0, 1
        left, right = [], []
        while count <= k and i*i <= n:
            # print("i is %s" %i)
            if n % i == 0:
                if(n // i == i):
                    left.append(i)
                else:
                    left.append(i)
                    right.append(n//i)
                count += 1
            i += 1
        # print("left %s " %left)
        # print("right %s " %right)
        if len(left) + len(right) < k:
            return -1
        if len(right) == 0:
            return left[0]
        if len(left) >= k:
            return left[k-1]
        index = len(right) - (k - len(left)) 
        return right[index]
    
    
