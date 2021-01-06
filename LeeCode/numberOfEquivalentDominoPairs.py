import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: [[int]]) -> int:
        targetDict = collections.defaultdict(int)
        for temp in dominoes:
            s = str(temp[0])+"_"+str(temp[1])
            if temp[1] > temp[0]:
                s = str(temp[1])+"_"+str(temp[0])
            targetDict[s] += 1
        count = 0
        for k in targetDict:
            v = targetDict[k]
            if v > 1:
                for tempV in range(v-1, -1, -1):
                    count += tempV
        return count


print(Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
