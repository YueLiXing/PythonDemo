import random


class Solution:

    def __init__(self, w: [int]):
        self.cache = []
        self.sum = 0
        self.len = 0
        for n in w:
            self.len += 1
            self.sum += n
            self.cache.append(self.sum)
            # print(self.cache)

    def pickIndex(self) -> int:
        targ = random.randint(0, self.sum)

        lo = 0
        hi = self.len - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if targ >= self.cache[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo

        # t = random.randint(0, self.sum)
        # low = 0
        # high = self.len - 1
        # while low != high:
        #     mid = (low+high) // 2
        #     if t > self.cache[mid]:
        #         low = mid+1
        #     else:
        #         high = mid
        # return low


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 3])
for i in range(5):
    param_1 = obj.pickIndex()
    print(param_1)
