class Solution:
    def merge(self, A: [int], m: int, B: [int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        targetIndex = m+n-1
        indexA = m-1
        indexB = n-1
        while True:
            if indexA >= 0 and indexB >= 0:
                if A[indexA] > B[indexB]:
                    A[targetIndex] = A[indexA]
                    indexA -= 1
                else:
                    A[targetIndex] = B[indexB]
                    indexB -= 1
            elif indexA >= 0:
                A[targetIndex] = A[indexA]
                indexA -= 1
            else:
                A[targetIndex] = B[indexB]
                indexB -= 1
            targetIndex -= 1
            if targetIndex < 0:
                break


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
