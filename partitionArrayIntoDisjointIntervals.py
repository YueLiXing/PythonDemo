class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftIndex = 0
        leftMin = A[leftIndex]
        leftMax = A[leftIndex]
        for index in range(leftIndex+1,len(A)):
            if leftMin > A[index]:
                leftIndex = index
                leftMin = A[index]
        for index in range(leftIndex+1):
            if A[index] > leftMax:
                leftMax = A[index]
        while True:
            flag = True
            for index in range(leftIndex+1,len(A)):
                if A[index] < leftMax:
                    # leftMax = A[index]
                    leftIndex = index
                    flag = False
            for index in range(leftIndex+1):
                if A[index] > leftMax:
                    leftMax = A[index]
            for index in range(leftIndex+1,len(A)):
                if A[index] < leftMax:
                    leftIndex = index
                    flag = False
            if flag:
                break
        return leftIndex+1


print(Solution().partitionDisjoint([5, 0, 3, 8, 6])) # 3
print(Solution().partitionDisjoint([1,1])) # 1
print(Solution().partitionDisjoint([26, 51, 40, 58, 42, 76, 30, 48, 79, 91])) # 1
print(Solution().partitionDisjoint([90, 47, 69, 10, 43, 92, 31, 73, 61, 97])) # 9
print(Solution().partitionDisjoint([29, 33, 6, 4, 42, 0, 10, 22, 62, 16, 46, 75, 100, 67, 70, 74, 87, 69, 73, 88])) # 11
