class Solution:
    def generate(self, numRows):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex = numRows-1
        ret = []
        if rowIndex >= 0:
            ret.append([1])
        if rowIndex >= 1:
            ret.append([1, 1])
        temp = [1, 1]
        index = 2
        while index <= rowIndex:
            index += 1
            newA = [1]
            for i in range(1, index-1):
                newA.append(temp[i-1]+temp[i])
            newA.append(1)
            ret.append(newA)
            temp = newA
        return ret
print(Solution().generate(1))
print(Solution().generate(2))
print(Solution().generate(3))
print(Solution().generate(4))
