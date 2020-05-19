class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        count = 0
        cacheMap = {0: 1}
        tempSum = 0
        for tempN in nums:
            tempSum += tempN
            if tempSum-k in cacheMap:
                count += cacheMap[tempSum-k]
            cacheMap[tempSum] = cacheMap.get(tempSum, 0)+1
            # print(cacheMap)
        return count
        # count = 0
        # lenN = len(nums)
        # for index in range(lenN):
        #     tempN = nums[index]
        #     tempSum = 0
        #     for indexJ in range(index, lenN):
        #         tempJ = nums[indexJ]
        #         tempSum += tempJ
        #         if tempSum == k:
        #             count += 1
        # return count


print(Solution().subarraySum([3, 4, 1, -1, 1, 3, 4], 7))
