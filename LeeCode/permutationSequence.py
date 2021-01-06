import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = [str(i+1) for i in range(n)]
        result = ""
        while len(temp) > 0:
            lTemp = len(temp)
            j = math.factorial(lTemp-1)
            t = math.ceil(k / j)-1
            k -= j*t
            result += temp[t]
            temp.pop(t)
            if lTemp-1 == 1:
                result += temp[0]
                break
        return result


print(Solution().getPermutation(3, 1))  # 123
print(Solution().getPermutation(3, 3))  # 213
print(Solution().getPermutation(3, 5))  # 312
print(Solution().getPermutation(4, 10))  # 2341
# print(Solution().getPermutation(5, 7))
