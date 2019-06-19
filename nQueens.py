class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
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


        target = []
        for val in self.ret:
            temp = []
            for i in range(n):
                point = val[i]
                t = []
                for k in range(n):
                    if k == point[0] and i == point[1]:
                        t.append("Q")
                    else:
                        t.append(".")
                temp.append("".join(t))
            target.append(temp)
        
        return target

        # "Q" "."

    def valNQueens(self, queens:[[int]], n: int, x: int, y: int) -> bool:
        for val in queens:
            tempX = val[0]
            tempY = val[1]
            if tempX == x or tempY == y or tempX+tempY == x+y or tempX-tempY == x-y:
            # if tempX == x or tempY == y or abs(tempY-y) == abs(tempX-x):
                return False
        return True



ret = Solution().solveNQueens(5)
print(len(ret))
for arr in ret:
    for a in arr:
        print(a)
    print("-------")
