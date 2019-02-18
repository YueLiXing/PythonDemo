class Solution:
    def combinationSum(self, candidates, target):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        ret = []
        tempArr = []
        for i in candidates:
            tempArr.append(0)
        index = 0
        while True:
            bufA = []
            for i in range(len(tempArr)):
                if tempArr[i] == 1:
                    bufA.append(candidates[i])
            if sum(bufA) == target:
                ret.append(bufA)

            if index == 2**n:
                break

            index += 1
            for i in range(len(tempArr)):
                tempArr[i] = tempArr[i]+1
                if tempArr[i] == 2:
                    tempArr[i] = 0
                else:
                    break

        return ret


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
