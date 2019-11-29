class Solution:
    def swap(self, A: [int], index: int, index1):
        t = A[index]
        A[index] = A[index1]
        A[index1] = t

    def sortArrayByParityII(self, A: [int]) -> [int]:
        startSingleIndex = 1
        for i in range(0, len(A), 2):
            v = A[i]
            if v % 2 != 0:
                for j in range(startSingleIndex, len(A), 2):
                    v0 = A[j]
                    if v0 % 2 == 0:
                        self.swap(A, i, j)
                        startSingleIndex = j+2
                        break
        return A


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
