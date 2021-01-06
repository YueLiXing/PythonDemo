class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        maxCount = 0
        temp = 0
        for i in range(len(nums)):
            val = nums[i]
            if val == 1:
                temp += 1
            else:
                maxCount = max(maxCount,temp)
                temp = 0
        maxCount = max(maxCount, temp)
        return maxCount
            


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
