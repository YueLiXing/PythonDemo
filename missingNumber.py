class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((1+len(nums))*len(nums)/2-sum(nums))


print(Solution().missingNumber([3, 0, 1]))
