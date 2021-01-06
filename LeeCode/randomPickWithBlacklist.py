import random
import collections


class Solution:

    def __init__(self, N: int, blacklist: [int]):
        lenBlackList = len(blacklist)
        self.n = N
        self.realN = N-lenBlackList
        self.cacheDict = {}

        cacheSet = set()
        for i in range(self.realN, N):
            cacheSet.add(i)
        for i in blacklist:
            if i in cacheSet:
                cacheSet.remove(i)
        cacheArr = list(cacheSet)
        # print("cacheArr", cacheArr)
        index = 0
        for i in blacklist:
            if i < self.realN:
                self.cacheDict[i] = cacheArr[index]
                index += 1
        # print(self.cacheDict, self.realN)

    def pick(self) -> int:
        temp = random.randint(0, self.realN-1)
        return self.cacheDict.get(temp, temp)


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
# obj = Solution(4, [0, 2])
obj = Solution(3, [0])
# obj = Solution(4, [0, 1])
countDict = collections.defaultdict(int)
for i in range(10000):
    param_1 = obj.pick()
    countDict[param_1] += 1
showResult(countDict)
