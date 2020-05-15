# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums: [int]):
        target = []
        nums = sorted(nums)
        lenN = len(nums)
        for index in range(lenN):
            tempN = nums[index]
            if tempN > 0:
                break
            if index > 0 and nums[index-1] == nums[index]:
                continue
            indexL = index + 1
            indexR = lenN-1
            while indexL < indexR:
                tempS = nums[index]+nums[indexL]+nums[indexR]
                if tempS == 0:
                    target.append([nums[index], nums[indexL], nums[indexR]])
                    while indexL < indexR and nums[indexL] == nums[indexL+1]:
                        indexL += 1
                    while indexL < indexR and nums[indexR] == nums[indexR-1]:
                        indexR -= 1
                    indexL += 1
                    indexR -= 1
                elif tempS > 0:
                    indexR -= 1
                else:
                    indexL += 1
        return target


# print(123)
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
