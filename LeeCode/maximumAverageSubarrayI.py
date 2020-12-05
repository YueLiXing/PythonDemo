class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        maxResult = sum(nums[:k])
        lastResult = maxResult
        for index in range(1,len(nums)-k+1):
            lastResult = lastResult+nums[index+k-1]-nums[index-1]
            if nums[index+k-1] > nums[index-1]:
                # lastResult = sum(nums[index:index+k])
                if lastResult > maxResult:
                    maxResult = lastResult
            # print(nums[index:index+k], sum(nums[index:index+k]))
        return maxResult / k


# print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3],4))
print(Solution().findMaxAverage([3, 3, 4, 3, 0], 3))

