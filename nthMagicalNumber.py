class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        aaa = 10**9+7
        if A%B == 0 or B%A == 0:
            return min(A,B)*N%aaa
        count = 0
        index = min(A,B)
        while True:
            if index % A == 0 or index % B == 0:
                count += 1
                if count == N:
                    break
            index += 1
        return index%aaa
print(Solution().nthMagicalNumber(4,2,3))