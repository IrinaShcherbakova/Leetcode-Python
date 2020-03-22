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


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    uniqueEl = {}
    for i in range(len(nums)):
        if nums[i] in uniqueEl:
            if i - uniqueEl[nums[i]] <= k:
                return True
            uniqueEl[nums[i]] = i
        else:
            uniqueEl[nums[i]] = i
    return False