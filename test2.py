class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            if self.judge(n):
                return n

    def judge(self, n: int) -> bool:
        tempArr = []
        while n > 0:
            tempArr.append(n % 10)
            n = n // 10
        tempSet = set(tempArr)
        for tempN in tempSet:
            if tempArr.count(tempN) != tempN:
                return False
        return True


Solution().judge(1231234)
print(Solution().judge(1))
