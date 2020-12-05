import math


class Solution:
    def imageSmoother(self, M: [[int]]) -> [[int]]:
        lenI = len(M)
        target = []
        for i in range(lenI):
            lenJ = len(M[i])
            temp = []
            target.append(temp)
            for j in range(lenJ):
                count = 0.0
                result = 0.0
                if j > 0:
                    result += M[i][j-1]  #
                    count += 1
                if j+1 < lenJ:
                    result += M[i][j+1]
                    count += 1
                if i > 0:
                    result += M[i-1][j]  #
                    count += 1
                    if j > 0:
                        result += M[i-1][j-1]  #
                        count += 1
                    if j+1 < lenJ:
                        result += M[i-1][j+1]  #
                        count += 1
                if i+1 < lenI:
                    result += M[i+1][j]
                    count += 1
                    if j > 0:
                        result += M[i+1][j-1]
                        count += 1
                    if j+1 < lenJ:
                        result += M[i+1][j+1]
                        count += 1
                count += 1
                result += M[i][j]
                # print(i, j, result, count, result/count)
                temp.append(math.floor(result/count))
        return target


Solution().imageSmoother([
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13],
    [14, 15, 16]
])
