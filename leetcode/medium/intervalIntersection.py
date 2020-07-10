class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            # print("a %s b %s " %(a,b))
            if a[1] < b[0]:
                i += 1
                continue
            if a[0] > b[1]:
                j += 1
                continue
            k = j
            while k < len(B) and self.isOverlap(a, B[k]):
                intersection = [max(a[0],B[k][0]),min(a[1],B[k][1])]
                # print("intersection: %s" %intersection)
                res.append(intersection)
                k += 1
            i += 1
        return res
    
    
    def isOverlap(self, a: List[int], b: List[int]):
        if a[1] >= b[0] and a[1] <= b[1]:
            return True
        if b[1] >= a[0] and b[1] <= a[1]:
            return True
        return False
        
        
