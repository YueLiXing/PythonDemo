class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1 if divisor >= 0 else -1
        if divisor < 0:
            divisor = -divisor
        ret = 0
        if dividend < 0:
            dividend = -dividend
            flag = -flag
        while dividend >= divisor:
            ret += 1
            dividend -= divisor
        
        return flag*ret


print(Solution().divide(-2147483648,-1))
