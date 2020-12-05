class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # index = len(matrix)+len(matrix[0])-1
        startIndexArr = []
        for index in range(len(matrix)-1,-1,-1):
            startIndexArr.append([index,0])
        for index in range(1,len(matrix[0])):
            startIndexArr.append([0,index])

        startIndexArr = startIndexArr[1:-1]
        # print(startIndexArr)
        for tempArr in startIndexArr:
            x = tempArr[0]
            y = tempArr[1]
            val = matrix[x][y]
            while True:
                x += 1
                y += 1
                if x < len(matrix) and y < len(matrix[0]):
                    if matrix[x][y] != val:
                        return False
                else:
                    break
        return True


# temp = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]
temp = [[83], [64], [57]]
print(Solution().isToeplitzMatrix(temp))
