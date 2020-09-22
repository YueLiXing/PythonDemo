class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x

        ans = 1
        buffer = x
        i = n
        while True:
            # print(i)
            if i % 2 == 1:
                ans = buffer*ans
                if i == 1:
                    break
            buffer = buffer*buffer
            i = i // 2

        return ans


print(Solution().myPow(2.0, 10))
