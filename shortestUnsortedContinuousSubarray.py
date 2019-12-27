class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        sortedNums = sorted(nums)
        lNums = len(nums)
        startIndex = -1
        endIndex = -1
        for index in range(lNums):
            if nums[index] != sortedNums[index]:
                startIndex = index
                break
        for index in range(lNums-1, -1, -1):
            if nums[index] != sortedNums[index]:
                endIndex = index
                break
        return endIndex-startIndex+1 if startIndex < endIndex else 0


# Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
# Solution().findUnsortedSubarray([1, 2, 3, 4])
# Solution().findUnsortedSubarray([1, 2, 3, 3, 3])
# Solution().findUnsortedSubarray([1, 2, 4, 5, 3])

Solution().findUnsortedSubarray([2, 3, 3, 2, 4])  # 1, 3
