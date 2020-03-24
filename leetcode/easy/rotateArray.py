def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    rotatedList = [None]*len(nums)
        for i in range(len(nums)):
            newIndex = (i+k) % len(nums)
            if rotatedList[newIndex] is None:
                rotatedList[newIndex] = nums[i]
    for i in range(len(nums)):
        nums[i] = rotatedList[i]
