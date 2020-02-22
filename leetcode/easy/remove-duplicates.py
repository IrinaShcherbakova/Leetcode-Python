def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    size = len(nums) - 1
    while i < size:
        if i != (len(nums) - 1):
            if nums[i] == nums[i+1]:
                del nums[i]
                size -= 1
            else:
                i += 1
        else:
            break
    return len(nums)


def removeElement(nums, val):
    i = 0
    size = len(nums)
    while i < size:
        if nums[i] == val:
            del nums[i]
            size -= 1
        i += 1
    return size






print("res is %s" % removeElement([3,2,2,3], 3))