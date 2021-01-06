class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        temp = [1,1]
        index = 1
        while index != rowIndex:
            index += 1
            newA = [1]
            for i in range(1,index):
                newA.append(temp[i-1]+temp[i])
            newA.append(1)
            temp = newA
        return temp


print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(4))
