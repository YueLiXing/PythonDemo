# 977. 有序数组的平方  显示英文描述
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

# 示例 1：
# 输入：[-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 示例 2：
# 输入：[-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        minRight = 0
        for index in range(len(A)):
            if A[index] >= 0:
                minRight = index
                break
        newA = A[minRight:]
        lastIndex = 0
        for index in range(minRight-1,-1,-1):  
            newValue = abs(A[index])
            flag = False
            for indexNewA in range(lastIndex, len(newA)):
                if newValue<=newA[indexNewA]:
                    newA.insert(indexNewA,newValue)
                    lastIndex = indexNewA
                    flag = True
                    break
            if flag == False:
                lastIndex = len(newA)
                newA.append(newValue)
        result = []
        for temp in newA:
            result.append(temp*temp)
        return result


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
print(Solution().sortedSquares([-2,0]))
print(Solution().sortedSquares([0]))


# list = [2,4,5,7]
# print(list[2:])
# print(list)
