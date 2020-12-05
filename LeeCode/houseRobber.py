class Solution:
    def rob(self, nums: [int]) -> int:
        countNum = len(nums)
        if countNum == 0:
            return 0
        elif countNum == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for index in range(2, countNum):
            first, second = second, max(nums[index]+first, second)
        return max(first, second)

