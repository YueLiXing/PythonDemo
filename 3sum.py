# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.tempDic = {}
        self.list = []
        nums.sort()
        cacheDict = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in cacheDict:
                cacheDict[val].append(i)
            else:
                cacheDict[val] = [i]
            # print(cacheDict)
        for index in range(0, len(nums)-2):
            num0 = nums[index]
            if num0 > 0:
                break
            if index == 0 or nums[index] > nums[index-1]:
                for index2 in range(index+1, len(nums)-1):
                    num1 = nums[index2]
                    num2 = 0-(num0+num1)
                    if num2 in cacheDict:
                        for i in cacheDict[num2]:
                            if i > index2:
                                tempArr = [num0, num1, num2]
                                key = "%d_%d_%d" % (num0, num1, num2)
                                if key not in self.tempDic:
                                    self.tempDic[key] = tempArr
                                    self.list.append(tempArr)
                                    break
                    
        return self.list


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0, 0,0,0,0,0,0,0,0,0]))
