class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        x = 0
        y = 0
        speedX = 1
        speedY = 0
        maxY = len(matrix)
        if maxY == 0:
            return []
        maxX = len(matrix[0])
        left = 0
        right = maxX-1
        top = 0
        bottom = maxY-1
        result = []
        while left <= right and top <= bottom:
            result.append(matrix[y][x])
            # print(matrix[y][x])
            tempX = x+speedX
            tempY = y+speedY
            if left <= tempX <= right and top <= tempY <= bottom:
                x = tempX
                y = tempY
            else:
                if tempX > right:
                    speedX, speedY = 0, 1
                    top += 1
                elif tempX < left:
                    speedX, speedY = 0, -1
                    bottom -= 1
                elif tempY > bottom:
                    speedX, speedY = -1, 0
                    right -= 1
                elif tempY < top:
                    speedX, speedY = 1, 0
                    left += 1
                x = x+speedX
                y = y+speedY
        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
