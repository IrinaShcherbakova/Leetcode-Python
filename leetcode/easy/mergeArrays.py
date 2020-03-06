def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    insertIndex = len(nums1) - 1
    if m == 0:
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1
        return
    i = m - 1
    j = n - 1
    while i <= insertIndex and j >= 0:
        if nums2[j] > nums1[i]:
            nums1[insertIndex] = nums2[j]
        elif nums1[i] > nums2[j]:
            nums1[insertIndex] = nums1[i]
            nums1[i] = nums2[j]
            swapIndex = i
            while swapIndex > 0 and nums1[swapIndex] < nums1[swapIndex-1]:
                temp = nums1[swapIndex]
                nums1[swapIndex] = nums1[swapIndex-1]
                nums1[swapIndex-1] = temp
                swapIndex -= 1
        else:
            nums1[insertIndex] = nums2[j]
            #i -= 1
        insertIndex -= 1
        j -= 1





nums1 = [0,0]
m = 0
nums2 = [-3,-3]
n = 2
merge(nums1, m, nums2, n)
print(nums1)