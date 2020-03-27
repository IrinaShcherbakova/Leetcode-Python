def missingNumber(self, nums: List[int]) -> int:
        sumNum = maxNum = 0
        minNum = nums[0]
        for num in nums:
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num
            sumNum += num
        if minNum > 0:
            return 0
        targetSum = (maxNum*(maxNum+1))//2
        if targetSum == sumNum:
            return maxNum + 1
        return targetSum - sumNum
