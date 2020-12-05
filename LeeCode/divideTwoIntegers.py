class Solution:
    # 被除数 除数
    # 15 3
    # 12 6
    # 6 12
    # 发现除数 大于 被除数大，再重现开始
    # 6 3
    # ...
    # 3 3
    
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1 if dividend^divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                print(dividend,temp)
                dividend -= temp
                ret += i
                temp = temp << 1
                i = i << 1
        ret = ret*flag
        return min(ret, 2147483647)


# print(Solution().divide(-2147483648, -1))
print(Solution().divide(1, 1))
