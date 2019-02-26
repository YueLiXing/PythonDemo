class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        dictB = {}
        sumB = 0
        for v in B:
            sumB += v
            dictB[v] = ""
        temp = int((sumB-sumA)/2)
        for val in A:
            if val+temp in dictB:
                return [val,val+temp]


print(Solution().fairCandySwap([1, 1],[2, 2]))
