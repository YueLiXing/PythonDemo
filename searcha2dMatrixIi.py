class Solution:
    # 改进版，从右上角开始寻找
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        x = m-1
        y = 0
        while 0 <= x and y < n:
            t = matrix[y][x]
            if t == target:
                return True
            elif t > target:
                x -= 1
            else:
                y += 1
        return False
    # # 从右下角开始，每次 x-1 y-1 进行查找，比较慢
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     n = len(matrix)
    #     if n == 0:
    #         return False
    #     m = len(matrix[0])
    #     if m == 0:
    #         return False
    #     x = m-1
    #     y = n-1
    #     while x >= 0 and y >= 0:
    #         t = matrix[y][x]
    #         if t < target:
    #             return False
    #         else:
    #             tMinX = matrix[y][0]
    #             if tMinX <= target:
    #                 for i in range(0,x+1):
    #                     if matrix[y][i] > target:
    #                         break
    #                     elif matrix[y][i] < target:
    #                         continue
    #                     else:
    #                         return True
    #             tMinY = matrix[0][x]
    #             if tMinY <= target:
    #                 for i in range(0, y+1):
    #                     if matrix[i][x] > target:
    #                         break
    #                     elif matrix[i][x] < target:
    #                         continue
    #                     else:
    #                         return True
    #             # print(matrix[y][x], tMinX, tMinY)
    #             x -= 1
    #             y -= 1
    #     return False


# matrix = [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
matrix = [
    [1,   4,  7, 11, 15,50],
    [2,   5,  8, 12, 19,60],
    [3,   6,  9, 16, 22,70],
    [10, 13, 14, 17, 24,80],
    [18, 21, 23, 26, 30,90]
]
print(Solution().searchMatrix(matrix, 5))
print(Solution().searchMatrix(matrix, 20))
