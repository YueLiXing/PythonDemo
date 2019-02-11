class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return
        lastValue = nums[0]
        index = 1
        while index < len(nums):
            if nums[index] == lastValue:
                nums.pop(index)
            else:
                lastValue = nums[index]
                index += 1


temp = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Solution().removeDuplicates(temp)
print(temp)
