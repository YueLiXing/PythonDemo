class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        countN = len(nums)
        L = [1]*countN
        R = [1]*countN
        result = [1]*countN

        for index in range(1, countN):
            L[index] = L[index-1]*nums[index]
        for index in range(countN-2, -1, -1):
            R[index] = R[index+1]*nums[index+1]
        # print(L, R)
        for index in range(countN):
            result[index] = L[index]*R[index]
        return result


Solution().productExceptSelf([1, 2, 3, 4])
