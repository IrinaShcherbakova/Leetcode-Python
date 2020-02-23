# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
   """
    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


print("res is %s" % searchInsert([1,3,5,6], 7))