class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        flips = []
        for i in range(len(A)-1, 0, -1):
            max_num, max_index = self.unsorted_max_in_range(A, i)
            if max_index == i: # max num is in the correct position
                continue
            # put max in the first position in A
            flips.append(max_index+1)
            self.reverse_in_range(A, max_index)
            # put max in the last position in A
            flips.append(i+1)
            self.reverse_in_range(A, i)
        return flips
    
    
    def unsorted_max_in_range(self, A: List[int], end: int) -> tuple:
        if end < 1:
            return None
        max_num, max_index = A[0], 0
        for i in range(end+1):
            if A[i] > max_num:
                max_num, max_index = A[i], i
        return max_num, max_index
    
    
    def reverse_in_range(self, A: List[int], end: int) -> None:
        i, j = 0, end
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return
    
    
    
    
    
    
    
    
    
    
    
    
