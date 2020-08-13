class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        # max_j_to_right stores the max value of j component of the pair, which we can obtain
        # looking in the right direction
        max_j_to_right = [None] * len(A)
        max_j = A[-1] - len(A) + 1
        max_j_to_right[-1] = max_j
        for j in range(len(A)-2, -1, -1):
            cur_j = A[j] - j
            max_j = max(max_j, cur_j)
            max_j_to_right[j] = max_j
            
        # when we walk, we sum the current i with max_j_to_right[i+1]
        best_sum = 0
        for i in range(len(A)-1):
            cur_sum = A[i] + i + max_j_to_right[i+1]
            best_sum = max(best_sum, cur_sum)
        
        return best_sum
                
                
