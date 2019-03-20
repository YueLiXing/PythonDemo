class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        buf = []
        if N > 0:
            while N > 0:
                buf.append(N % 2)
                N = N//2
        else:
            buf.append(0)
        
        ret = 0
        b = 1
        for i in range(len(buf)):
            ret += (1 if 0 == buf[i] else 0)*b
            b *= 2
        return ret


print(Solution().bitwiseComplement(0))
Solution().bitwiseComplement(6)
# print(Solution().bitwiseComplement(5))
