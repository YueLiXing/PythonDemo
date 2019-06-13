class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        x,y = 0,0
        border = n//2+n % 2
        flag = n%2
        # print(border)
        for x in range(border):
            for y in range(border):
                # print(matrix[y][x])
                if flag == 1 and x == border-1:
                    continue
                t = matrix[y][x]
                matrix[y][x] = matrix[n-1-x][y]
                matrix[n-1-x][y] = matrix[n-1-y][n-1-x]
                matrix[n-1-y][n-1-x] = matrix[x][n-1-y]
                matrix[x][n-1-y] = t

# matrix = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for v in matrix:
    print(v)
Solution().rotate(matrix)
print("result:")
for v in matrix:
    print(v)

# 原地旋转输入矩阵，使其变为:
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]
