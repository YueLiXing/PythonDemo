class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for tempA in A:
            tempA.reverse()
            for i in range(len(tempA)):
                if tempA[i] == 0:
                    tempA[i] = 1
                else:
                    tempA[i] = 0
        return A


print(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
