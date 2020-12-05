class Solution:
    def reverse(self, x):
        if not -2147483648 < x < 2147483647:
            return 0
        result = 0
        flag = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            result *= 10
            result += x % 10
            x /= 10
            x = int(x)
        result *= flag
        # print(-2147483648 < result < 2147483647, result)
        if -2147483648 < result < 2147483647:
            return result
        return 0


# 2147483647
# 9646324351
test = Solution()
# print(test.reverse(123)) # 321
# print(test.reverse(-123))  # -321
# print(test.reverse(120)) # 21
print(test.reverse(9646324351))  # 21

