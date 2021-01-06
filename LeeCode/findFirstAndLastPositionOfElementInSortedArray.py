class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        l = len(nums)
        start = -1
        for index in range(l):
            val = nums[index]
            if start < 0 and val == target:
                start = index
            if start >= 0 and val > target:
                return [start,index-1]
        if start >= 0:
            return [start, l-1]
        return [-1,-1]