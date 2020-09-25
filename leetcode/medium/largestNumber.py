class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = []
        for num in nums:
            string_nums.append(str(num))
        
        n = len(string_nums) 
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if not self.compare(string_nums[j], string_nums[j+1]): 
                    string_nums[j], string_nums[j+1] = string_nums[j+1], string_nums[j] 
        res = ""
        for num in string_nums:
            res += num
        if res[0] == '0':
            return '0'
        return res

    
    def compare(self, s1: str, s2: str) -> bool:
        s1s2 = int(s1 + s2)
        s2s1 = int(s2 + s1)
        return True if s1s2 >= s2s1 else False
                   
                
                
