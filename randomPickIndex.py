import random


class Solution:

    def __init__(self, nums: [int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        index = -1
        count = 0
        for i in range(len(self.nums)):
            temp = self.nums[i]
            if temp == target:
                count += 1
                if count == 1:
                    index = i
                else:
                    if random.randint(1, count) == 1:
                        index = i
        return index


# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
param_1 = obj.pick(target)
