# 961. 重复 N 次的元素
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        countDict = {}
        n = len(A)/2
        for tempC in A:
            countDict[tempC] = countDict.get(tempC,0)+1
            if countDict[tempC] == n:
                return tempC


print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
