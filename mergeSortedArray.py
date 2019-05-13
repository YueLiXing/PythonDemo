class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        count = 0
        while index1 < m+count and index2 < n:
            t1 = nums1[index1]
            t2 = nums2[index2]
            
            if t1 >= t2:
                nums1.insert(index1, t2)
                index2 += 1
                nums1.pop()
                count += 1
            else:
                index1 += 1
        # print(index1)
        # while index1 < m+count:
        #     nums1.pop()
        #     index1 += 1
        while index2 < n:
            t2 = nums2[index2]
            nums1.insert(index1, t2)
            nums1.pop()
            index1 += 1
            index2 += 1

l1 = [0, 0, 2, 0, 0, 0, 0, 0, 0]
l2 = [-1, 1, 1, 1, 2, 3]
Solution().merge(l1, 3, l2, 6)
# l1 = [1,2,7,0,0,0]
# l2 = [2,5,6]
# Solution().merge(l1,3,l2,3)
print(l1)
# l1 = [0]
# l2 = [1]
# Solution().merge(l1,0,l2,1)
# print(l1)
