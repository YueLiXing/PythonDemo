class Solution:
    def majorityElement(self, nums: [int]) -> int:
        t = None
        count = 0
        for temp in nums:
            if count == 0:
                t = temp
                count = 1
                continue
            if t == temp:
                count += 1
            else:
                count -= 1
        return t
