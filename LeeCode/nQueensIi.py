class Solution:
    def totalNQueens(self, n):
        self.ret = []
        tempRet = []
        x = 0
        y = 0
        while True:
            isEnd = False
            if x >= n or isEnd:
                break
            while len(tempRet) > 0:
                last = tempRet.pop()
                y = last[1]
                x = last[0]+1
                if x < n:
                    break
            while True:
                if y == n:
                    break
                if x >= n:
                    if len(tempRet) == 0:
                        isEnd = True
                        break
                    else:
                        last = tempRet.pop()
                        y = last[1]
                        x = last[0]+1
                        continue
                r = self.valNQueens(tempRet, n, x, y)
                # print(x,y,r)
                if r:
                    tempRet.append([x, y])
                    # print(tempRet)
                    y += 1
                    x = 0
                else:
                    x += 1
                    continue
            if len(tempRet) == n:
                isAdd = True
                self.ret.append(tempRet.copy())
            # print(self.ret)
        return len(self.ret)

    def valNQueens(self, queens: [[int]], n: int, x: int, y: int) -> bool:
        for val in queens:
            tempX = val[0]
            tempY = val[1]
            if tempX == x or tempY == y or tempX+tempY == x+y or tempX-tempY == x-y:
                return False
        return True


s = Solution()
# for temp in range(1, 1001):
#     print(temp, s.totalNQueens(temp))

print(s.totalNQueens(8)) # 92

