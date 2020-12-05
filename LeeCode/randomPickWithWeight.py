import random
import collections


class Solution:

    def __init__(self, w: [int]):
        self.cache = []
        temp = 0
        tempSum = 0
        for n in w:
            temp += 1
            tempSum += n
            self.cache.append(tempSum)
        self.lenCache = temp
        self.totalSum = tempSum

    def pickIndex(self) -> int:
        targ = random.randint(1, self.totalSum)
        lo = 0
        hi = self.lenCache - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if targ > self.cache[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo


def showResult(countDict: collections.defaultdict):
    total = 0
    for k in countDict:
        v = countDict[k]
        total += v
    print("result:")
    for k in countDict:
        v = countDict[k]
        print(k, v/total*100)


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 1, 1, 1])
# obj = Solution([3, 1])
countDict = collections.defaultdict(int)
for i in range(10000):
# for i in range(1):
    param_1 = obj.pickIndex()
    countDict[param_1] += 1
    # print(param_1)
showResult(countDict)
