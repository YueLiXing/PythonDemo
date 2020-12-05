class Solution:
    # 有序矩阵，二分查找
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        lowN = 0
        highN = n-1
        lowM = 0
        highM = m-1
        if matrix[lowN][lowM] > target or matrix[highN][highM] < target:
            return False
        while lowN <= highN and lowM <= highM:
            if lowN != highN:
                mid = (lowN+highN)//2
                if matrix[mid][lowM] > target:
                    highN = mid-1
                elif matrix[mid][lowM] < target:
                    lowN = mid
                    if matrix[mid][highM] >= target:
                        highN = mid
                    if matrix[mid][highM] < target:
                        lowN = mid+1
                else:
                    return True
            else:
                mid = (lowM+highM)//2
                if matrix[lowN][mid] > target:
                    highM = mid-1
                elif matrix[lowN][mid] < target:
                    lowM = mid+1
                else:
                    return True
        return False


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

# target = 1
target = 11
# 输出: true

print(Solution().searchMatrix(matrix, target))
