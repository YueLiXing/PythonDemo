class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 1
        while True:
            if temp not in nums:
                break
            else:
                temp += 1
        return temp