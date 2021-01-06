class Solution:
    def singleNumber(self, nums: [int]) -> int:
        cache = 0
        r = 0
        for i in nums:
            r ^= i

        return r


# 这种方法更快
# class Solution:
#     def singleNumber(self, nums: [int]) -> int:
#         countDict = {}
#         for tempN in nums:
#             if tempN in countDict:
#                 countDict[tempN] += 1
#             else:
#                 countDict[tempN] = 1
#         for tempN in countDict:
#             if countDict[tempN] == 1:
#                 return tempN
#         return 0


r = Solution().singleNumber([2, 2, 1])
print(r)
