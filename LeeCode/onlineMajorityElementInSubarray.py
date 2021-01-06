class MajorityChecker:

    def __init__(self, arr: [int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        cacheDict = {}
        for index in range(left, right+1):
            temp = self.arr[index]
            if temp in cacheDict:
                cacheDict[temp] += 1
            elif 2 * threshold > right - left + 1:
                cacheDict[temp] = 1
        if len(cacheDict) == 0:
            return -1
        else:
            lastK = -1
            lastV = -1
            for k, v in cacheDict:
                if v > lastV:
                    lastV = v
                    lastK = k
            return lastK


# Your MajorityChecker object will be instantiated and called as such:

arr = [1, 1, 2, 2, 1, 1]
], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
obj = MajorityChecker(arr)
param_1 = obj.query(0, 5, 4)
