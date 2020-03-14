# Given an array of size n, find the majority element.
# The majority element is the element that appears more
# than ⌊ n/2 ⌋ times.

def majorityElement(self, nums: List[int]) -> int:
    dict = {}
    majority = len(nums) // 2
    for num in nums:
        if num not in dict:
            dict[num] = 1
            continue
        if dict[num] >= majority:
            return num
        dict[num] += 1
    return nums[0]