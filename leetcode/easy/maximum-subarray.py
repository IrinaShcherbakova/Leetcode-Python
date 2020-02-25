# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.

def maxSubArray(nums):
    maxSum = maxAtIndex = nums[0]
    i = 1
    while i < len(nums):
        maxAtIndex = max(nums[i], maxAtIndex + nums[i])
        maxSum = max(maxSum, maxAtIndex)
        i += 1
    return maxSum


print("res is %s" % maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))