class Solution:
    def checkGrid(self, grid: [[int]], steps:set):
        # print(grid)
        flag = True
        for temp in grid:
            for tempA in temp:
                if tempA == 0:
                    flag = False
                    break
            if flag == False:
                break
        self.count += 1 if flag else 0
        # if flag:
        #     print(steps)

    def run(self, grid: [[int]], currertX: int, currertY: int, steps: set):
        # print("current:",currertX, currertY, "size:",len(grid[0]), len(grid))
        if currertX < 0 or currertY < 0 or currertX >= len(grid[0]) or currertY >= len(grid):
            return
        # print(currertX, currertY, "val:", grid[currertY][currertX])
        if grid[currertY][currertX] == -1 or grid[currertY][currertX] == 1 or grid[currertY][currertX] == 3:
            return
        elif grid[currertY][currertX] == 2:
            self.checkGrid(grid, steps)
            return
        elif grid[currertY][currertX] == 0:
            steps.add("%d_%d" % (currertX, currertY))

            grid[currertY][currertX] = 3
            # print()
            # for temp in grid:
            #     print(temp)
            # print()
            
            if ("%d_%d" % (currertX, currertY+1)) not in steps:
                self.run(self.copyGrid(grid), currertX, currertY+1, steps.copy())
            if ("%d_%d" % (currertX, currertY-1)) not in steps:
                self.run(self.copyGrid(grid), currertX, currertY-1, steps.copy())

            if ("%d_%d" % (currertX-1, currertY)) not in steps:
                self.run(self.copyGrid(grid), currertX-1, currertY, steps.copy())
            if ("%d_%d" % (currertX+1, currertY)) not in steps:
                self.run(self.copyGrid(grid), currertX+1, currertY, steps.copy())

            # self.run(self.copyGrid(grid), currertX-1, currertY, steps.copy())
            # self.run(self.copyGrid(grid), currertX+1, currertY, steps.copy())

    def copyGrid(self, grid:[[int]]):
        ret = []
        for temp in grid:
            t = []
            for i in temp:
                t.append(i)
            ret.append(t)
        return ret
        

    def uniquePathsIII(self, grid: [[int]]) -> int:
        self.count = 0

        m = len(grid)
        n = len(grid[0])
        startX = 0
        startY = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    startY = i
                    startX = j
                    break
        # print(startX,startY)
        grid[startY][startX] = 0
        self.run(grid,startX,startY, set())

        return self.count


temp = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
# temp = [[1, 0], [2, 0]]
print(Solution().uniquePathsIII(temp))
