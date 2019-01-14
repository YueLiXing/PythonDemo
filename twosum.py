class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 一遍哈希法
        temp = {}
        for index in range(len(nums)):
            current = nums[index]
            if target-current in temp.keys():
                return [temp[target-current], index]
            else:
                temp[nums[index]] = index
        # 暴力穷举
        # result = []
        # for index in range(len(nums)):
        #     for index2 in range(index+1,len(nums)):
        #         if index != index2:
        #             if nums[index]+nums[index2] == target:
        #                 result = [index, index2]
        #                 break
        # return result



test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
print(test.twoSum([3, 2, 4], 6))
