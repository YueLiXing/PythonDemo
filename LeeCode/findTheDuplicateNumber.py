class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        tempS = set()
        for i in nums:
            if i in tempS:
                return i
            else:
                tempS.add(i)
        return -1