class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i
        return l