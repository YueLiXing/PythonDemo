class Solution:
    def reverse(self, x):
        if not (-2**31 < x < 2**31-1):
            return 0
        result = 0
        flag = -1 if x < 0 else 1
        x = abs(x)
        while True:
            if x > 0:
                result *= 10
                result += x % 10
                x /= 10
                x = int(x)
            else:
                break
        return result*flag


test = Solution()

print(test.reverse(321))
print(test.reverse(-123456789))
print(2**3)
