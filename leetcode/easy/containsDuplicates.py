def containsDuplicate(self, nums: List[int]) -> bool:
    if len(nums) == 0:
        return False
    uniqueValues = {nums[0]}
    for i in range(1, len(nums)):
        # print(nums[i])
        if nums[i] in uniqueValues:
            return True
        uniqueValues.add(nums[i])
    return False