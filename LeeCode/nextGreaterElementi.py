class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        l2 = len(nums2)
        for index1 in range(len(nums1)):
            val1 = nums1[index1]
            flag = True
            for index2 in range(nums2.index(val1)+1,l2):
                if nums2[index2] > val1:
                    ret.append(nums2[index2])
                    flag = False
                    break
            if flag:
                ret.append(-1)
        return ret


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
