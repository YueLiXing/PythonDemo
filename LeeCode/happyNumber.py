class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache = set()
        while True:
            temp = []
            while n > 0:
                temp.append(n%10)
                n = n // 10
            ret = 0
            # print(temp)
            for a in temp:
                ret += a*a
            if ret == 1:
                return True
            elif ret in cache:
                return False
            else:
                cache.add(ret)
            n = ret
        return False


print(Solution().isHappy(7))
