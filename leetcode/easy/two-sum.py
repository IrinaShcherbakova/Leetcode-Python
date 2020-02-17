#brute-force solution
# def twoSum(nums, target):
#     res = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 res.append(i)
#                 res.append(j)
#                 return res

#with dictionary
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        reminder = target - nums[i]
        if reminder in dict:
            return [dict[reminder], i]
        dict[nums[i]] = i


print("res is %s" % twoSum([3,2,4], 6))
