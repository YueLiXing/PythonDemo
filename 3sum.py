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
        for index in range(0, len(nums)-2):
            num0 = nums[index]
            if num0>0:
                break
            for index2 in range(index+1, len(nums)-1):
                num1 = nums[index2]
                num2 = 0-(num0+num1)

                if num2 in nums[index2+1:]:
                    tempArr = [num0, num1, num2]
                    target = []
                    tempArr.sort()
                    for temp in tempArr:
                        target.append(str(temp))
                    key = "".join(target)
                    if key not in self.tempDic:
                        self.tempDic[key] = target
                        self.list.append([num0,num1,num2])
        return self.list


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
