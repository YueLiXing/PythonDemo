class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        index0 = 0
        index1 = 0
        count = -1
        totalCount = l1+l2
        flag = (l1+l2) % 2
        target = (l1+l2) // 2
        # print("target: %d" % target)
        ret = []
        if totalCount == 1:
            return nums1[0] if l1 > 0 else nums2[0]
        while index0 < l1 or index1 < l2:
            temp = 0
            if index0 < l1 and index1 < l2:
                if nums1[index0] < nums2[index1]:
                    temp = nums1[index0]
                    index0 += 1
                else:
                    temp = nums2[index1]
                    index1 += 1
            elif index0 < l1:
                temp = nums1[index0]
                index0 += 1
            else:
                temp = nums2[index1]
                index1 += 1
            count += 1
            # print("count: %d， temp:%d" % (count, temp))
            if flag == 1 and count == target:
                return temp
            else:
                if count+1 == target or count == target:
                    ret.append(temp)
                    if count == target:
                        # print("ret", ret)
                        return sum(ret) / 2

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         totalCount = len(nums1)+len(nums2)
#         if totalCount == 1:
#             return nums1[0] if len(nums1) > 0 else nums2[0]
#         flag = totalCount % 2
#         centerIndex = totalCount // 2
#         # 中位数
#         # 如果 flag 为 0 ，那么中位数为中间的两个数
#         # 如果 flag 为 1 ，那么中位数为中间的一个数
#         index1 = 0
#         index2 = 0
#         result = []
#         while index1 < len(nums1) or index2 < len(nums2):
#             if index1 >= len(nums1):
#                 result.append(nums2[index2])
#                 index2 += 1
#             elif index2 >= len(nums2):
#                 result.append(nums1[index1])
#                 index1 += 1
#             else:
#                 if nums1[index1] <= nums2[index2]:
#                     result.append(nums1[index1])
#                     index1 += 1
#                 else:
#                     result.append(nums2[index2])
#                     index2 += 1
#             if flag == 1 and len(result) == centerIndex+1:
#                 print(result)
#                 return result[-1]
#             elif flag == 0 and len(result) == centerIndex+1:
#                 print(result)
#                 return (result[-1]+result[-2])/2

print(Solution().findMedianSortedArrays([1, 3], [2]))
# print(Solution().findMedianSortedArrays([1, 3], [2, 4]))
