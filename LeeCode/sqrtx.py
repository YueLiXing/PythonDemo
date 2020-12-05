import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(math.sqrt(x))
        left = 0
        right = x // 2 + 1
        while left < right:
            mid = (left+right+1) // 2
            temp = mid*mid
            if temp > x:
                right = mid-1
            elif temp == x:
                return mid
            else:
                left = mid
        return left



for i in range(1, 21):
    print("print", i, Solution().mySqrt(i), int(math.sqrt(i)))
