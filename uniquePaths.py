class Solution:
    def getJieCheng(self,n:int):
        ret = 1
        for i in range(1,n+1):
            ret *= i
        return ret
        
    # def uniquePaths(self, m: int, n: int) -> int:
    #     return int(self.getJieCheng(m+n-2)/(self.getJieCheng(n-1)*self.getJieCheng(m-1)))

    # 另一种解法
    def uniquePaths(self, m: int, n: int) -> int:
        temp = []
        for i in range(m):
            t = []
            for i in range(n):
                t.append(0)
            temp.append(t)
        print(temp)
        temp[0][0] = 1
        for row in range(1,m):
            temp[row][0] = 1 if temp[row-1][0] == 1 and temp[row][0] == 0 else 0
        for col in range(1, n):
            temp[0][col] = 1 if temp[0][col-1] == 1 and temp[0][col] == 0 else 0

        for row in range(1,m):
            for col in range(1,n):
                if temp[row][col] == 0:
                    temp[row][col] = temp[row-1][col]+temp[row][col-1]
                else:
                    temp[row][col] = 0
        print(temp)
        print(temp[m-1][n-1])
        return int(self.getJieCheng(m+n-2)/(self.getJieCheng(n-1)*self.getJieCheng(m-1)))


print(Solution().uniquePaths(3,7))
