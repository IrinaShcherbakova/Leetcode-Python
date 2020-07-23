class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.recurse(nums, 0, [])
    
    def recurse(self, nums: List[int], index: int, permutations: List[List[int]]) -> List[List[int]]:
        if index == len(nums):
            return permutations
        if index == 0:
            permutations.append([nums[0]])
            return self.recurse(nums, 1, permutations)
        newPermutations = []
        for permut in permutations:
            for i in range(len(permut)):
                newPermut = permut[0:i] + [nums[index]] + permut[i:len(permut)]
                newPermutations.append(newPermut)
            newPermutations.append(permut + [nums[index]])
        return self.recurse(nums, index+1, newPermutations)
            
            
        
        
        
