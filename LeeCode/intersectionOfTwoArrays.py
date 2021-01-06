class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        if len(nums2) < len(nums1):
            t = nums2
            nums2 = nums1
            nums1 = t
        # return set(nums1) & set(nums2)
        cache1 = set()
        for tempInt in nums1:
            cache1.add(tempInt)
        resultSet = set()
        target = []
        for tempInt in nums2:
            if tempInt in cache1:
                if tempInt in resultSet:
                    continue
                else:
                    resultSet.add(tempInt)
                    target.append(tempInt)
        return target

    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        count1 = {}
        count2 = {}
        for temp in nums1:
            count1[temp] = count1.get(temp, 0) + 1
        for temp in nums2:
            count2[temp] = count2.get(temp, 0) + 1

        result = {}
        for k, v in count1.items():
            v2 = count2.get(k, 0)
            ret = min(v, v2)
            if ret > 0:
                result[k] = ret
        target = []
        for k, v in result.items():
            for i in range(v):
                target.append(k)
        return target
