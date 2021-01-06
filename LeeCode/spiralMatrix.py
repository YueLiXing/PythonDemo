class Solution:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return "Point(x:%d,y:%d)" % (self.x, self.y)

    def spiralOrder(self, matrix: [[int]]) -> [int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        ret = []

        currentPoint = Point(0, 0)
        direction = Point(1, 0)
        lt = Point(0, 0)
        rt = Point(m-1, 0)
        lb = Point(0, n-1)
        rb = Point(m-1, n-1)

        # print(lt,rt)
        # print(lb,rb)

        # print(matrix[currentPoint.y][currentPoint.x])
        ret.append(matrix[currentPoint.y][currentPoint.x])
        # print("%d %d : %d" % (currentPoint.y, currentPoint.x,matrix[currentPoint.y][currentPoint.x]))
        while True:
            nextP = Point(currentPoint.x+direction.x,
                          currentPoint.y+direction.y)
            # print("%d %d %s" % (nextP.y, nextP.x, direction))
            if lt.x <= nextP.x <= rb.x and lt.y <= nextP.y <= rb.y:
                currentPoint = nextP

                # print()
                # print("%d %d : %d" % (currentPoint.y, currentPoint.x,matrix[currentPoint.y][currentPoint.x]))
                ret.append(matrix[currentPoint.y][currentPoint.x])
            else:
                if direction.x == 1 and direction.y == 0:
                    # direction = Point(0,1)
                    direction.x = 0
                    direction.y = 1
                    lt.y += 1
                    rt.y = lt.y
                elif direction.x == 0 and direction.y == 1:
                    # direction = Point(-1,0)
                    direction.x = -1
                    direction.y = 0
                    rt.x -= 1
                    rb.x = rt.x
                elif direction.x == -1 and direction.y == 0:
                    # direction = Point(0,-1)
                    direction.x = 0
                    direction.y = -1
                    lb.y -= 1
                    rb.y = lb.y
                else:
                    # direction = Point(1, 0)
                    direction.x = 1
                    direction.y = 0
                    lt.x += 1
                    lb.x = lt.x
                if lt.x > rt.x and lt.y > rb.y:
                    break
        return ret


l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
l = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(Solution().spiralOrder(l))

# 最近提交结果：
# 通过
# 显示详情
# 执行用时:
# 40 ms
# , 在所有Python3提交中击败了
# 98.73%
# 的用户
# 内存消耗:
# 13 MB
# , 在所有Python3提交中击败了
# 94.69%
# 的用户
# 炫耀一下:
