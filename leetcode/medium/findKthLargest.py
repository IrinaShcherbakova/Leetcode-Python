class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # print("nums is %s" %nums)
        # print("K is %s" %k)
        low, high = 0, len(nums)-1
        while low < high:
            j = self.partition(nums, low, high)
            # print("j is %s, nums is %s" %(j, nums))
            if j < k-1:
                low = j+1
            elif j > k-1:
                high = j-1
            else:
                return nums[k-1]
        return nums[k-1]
    
    
    def partition(self, nums: List[int], low: int, high: int) -> int:
        # print("partition %s" %nums)
        i = low-1
        pivot = nums[high]
        # print("pivot is %s" %pivot)
        for j in range(low, high):
            if nums[j] > pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        # print(nums)
        # print("return i+1 = %s" %(i+1))
        return i+1
            
        
                
