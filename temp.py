class Solution:
    def singleNumber(self, nums: [int]) -> int:
        countDict = {}
        for tempN in nums:
            if tempN in countDict:
                countDict[tempN] += 1
            else:
                countDict[tempN] = 1
        for tempN in countDict:
            if countDict[tempN] == 1:
                return tempN
        return 0
